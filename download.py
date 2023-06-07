# %%
import urllib.request
from tqdm import tqdm
from IPython.display import display, Markdown, Latex
# %%

base_url = "https://d2nnsrwhv0jum3.cloudfront.net/"
docs_url = "https://raw.githubusercontent.com/uchicago-dsi/summer-lab-data/main/__data__/"

default_data_dir = './__data__/'
files = [
   {
      "name": "states.gpkg",
      "file_link": "states_2019_simplified100_wgs84.gpkg",
   },
   {
      "name": "counties.gpkg",
      "file_link": "counties.gpkg",
   },
   {
      "name": "tracts.gpkg",
      "file_link": "tracts.gpkg",
   },
   {
      "name": "zcta.gpkg",
      "file_link": "zcta.gpkg",
   }
]

# %%

class Downloader:
  def __init__(self, files=files, data_path: str=default_data_dir, base_url: str = base_url, docs_url: str = docs_url):
    self.data_path = data_path
    self.base_url = base_url
    self.files = files
    self.docs_url = docs_url

  def download(self, url: str, file_name: str):
      urllib.request.urlretrieve(url, file_name)

  def download_all(self):
    for file in tqdm(self.files):
      self.download(f"{self.base_url}{file['file_link']}", f"{self.data_path}{file['name']}")
    
    files_downloaded = [file['name'] for file in self.files]
    display(Markdown(f"Files downloaded: {', '.join(files_downloaded)}"))

  def data_help(self, file: str):
    # find the file in the list of files
    file = next((item for item in self.files if item["name"] == file), None)
    if file is None:
      print("File not found -- make sure to include the extension, like 'states.gpkg'")
      return
 
    markdown_url = f"{self.docs_url}{file['name']}.readme.md"
    # fetch the markdown url
    with urllib.request.urlopen(markdown_url) as response:
      readme = response.read()
      display(Markdown(readme.decode('utf-8')))

# %%
default_downloader = Downloader()

def data_help(file: str):
  default_downloader.data_help(file)

def download_files():
  default_downloader.download_all()
# %%
if __name__ == "__main__":
  download_files()
# %%

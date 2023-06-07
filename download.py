# %%
import urllib.request
from tqdm import tqdm
from IPython.display import display, Markdown, Latex
# %%

base_url = "https://d2nnsrwhv0jum3.cloudfront.net/"
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
  def __init__(self, files=files, data_path: str=default_data_dir, base_url: str = base_url):
    self.data_path = data_path
    self.base_url = base_url
    self.files = files

  def download(self, url: str, file_name: str):
      urllib.request.urlretrieve(url, file_name)

  def download_all(self):
    for file in tqdm(self.files):
      self.download(f"{self.base_url}{file['file_link']}", f"{self.data_path}{file['name']}")
      self.download(f"{self.base_url}{file['file_link']}.readme.md", f"{self.data_path}{file['name']}.readme.md")
    
    files_downloaded = [file['name'] for file in self.files]
    display(Markdown(f"Files downloaded: {', '.join(files_downloaded)}"))

  def data_help(self, file: str):
    # find the file in the list of files
    file = next((item for item in self.files if item["name"] == file), None)
    if file is None:
      print("File not found -- make sure to include the extension, like 'states.gpkg'")
      return
    # open the file from the data directory
    with open(f"{self.data_path}{file['name']}.readme.md", 'rb') as readme:
      display(Markdown(readme.read().decode('utf-8')))

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

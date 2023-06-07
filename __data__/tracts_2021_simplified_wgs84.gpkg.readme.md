# 2021 Census Tracts Geospatial Data (tracts.gpkg)

The 2021 Census Tract data provides information about the shapes and boundaries of different tracts in the United States. It includes the geographic details that help us understand where each tract is located and how it is shaped on a map. You can join this data to additional tables or resources based on the GEOID column, or spatially join it to other data based on the geometry column. A tract is approximately equivalent to a unit of ~4,000 people, and in general tends to be equivalent to a neighborhood scale in the city.

|   Column   | Data Type |                 Description                  |
|------------|-----------|----------------------------------------------|
| STATEFP    |  Text     | State FIPS code                               |
| COUNTYFP   |  Text     | County FIPS code                              |
| TRACTCE    |  Text     | Census tract code                             |
| GEOID      |  Text     | Unique identifier for the census tract        |
| NAME       |  Text     | Tract name                                    |
| NAMELSAD   |  Text     | Legal/Statistical Area Description for the tract |
| MTFCC      |  Text     | MAF/TIGER Feature Class Code                  |
| FUNCSTAT   |  Text     | Functional Status of the tract                |
| ALAND      |  Numeric  | Land area in square meters                    |
| AWATER     |  Numeric  | Water area in square meters                   |
| INTPTLAT   |  Numeric  | Latitude of the tract's internal point        |
| INTPTLON   |  Numeric  | Longitude of the tract's internal point       |
| geometry   |  Geometry | Spatial representation of the tract           |

## Notes

- This data has been simplified at a tolerance of 5 meters.
- This data is in the `EPSG:4326` projection. For area or distance calculations, be sure to project it into another coordinate reference system (CRS). For example, area calculations could use the USA Contiguous Albers Equal Area projection (`EPSG:102003`)

## Data Source

This data comes from The [US Census Tiger/Line Geometries](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2021.html#list-tab-790442341).

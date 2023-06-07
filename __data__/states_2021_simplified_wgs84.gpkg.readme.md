# 2021 State Geospatial Data (states.gpkg)

The 2021 Census state data provides information about the shapes and boundaries of different states in the United States. It includes the geographic details that help us understand where each state is located and how it is shaped on a map. You can join this data to additional tables or resources based on the GEOID column, or spatially join it to other data based on the geometry column.

| Column     | Description                                          | Data Type            |
|------------|------------------------------------------------------|----------------------|
| REGION     | The region code of the state.                         | Numeric              |
| DIVISION   | The division code of the state.                       | Numeric              |
| STATEFP    | The state FIPS code.                                  | Numeric              |
| STATENS    | The state ANSI code.                                  | Numeric              |
| GEOID      | The state geographic identifier code.                 | Numeric              |
| STUSPS     | The state postal abbreviation.                        | Text                 |
| NAME       | The name of the state.                                | Text                 |
| LSAD       | Legal/Statistical Area Description code.              | Text                 |
| MTFCC      | MAF/TIGER Feature Class Code.                         | Text                 |
| FUNCSTAT   | Functional Status of the state.                       | Text                 |
| ALAND      | Land area of the state in square meters.              | Numeric              |
| AWATER     | Water area of the state in square meters.             | Numeric              |
| INTPTLAT   | The latitude of the state's internal point.           | Numeric (Latitude)   |
| INTPTLON   | The longitude of the state's internal point.          | Numeric (Longitude)  |
| geometry   | Geospatial representation of the state's boundaries.  | Geospatial Object    |


## Notes

- This data has been simplified at a tolerance of 10 meters.
- This data is in the `EPSG:4326` projection. For area or distance calculations, be sure to project it into another coordinate reference system (CRS). For example, area calculations could use the USA Contiguous Albers Equal Area projection (`EPSG:102003`)

## Data Source

This data comes from The [US Census Tiger/Line Geometries](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2021.html#list-tab-790442341).

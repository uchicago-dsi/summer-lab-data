# 2021 Zip Code Tabulation Area (ZCTA) Geospatial Data (zcta.gpkg)

The 2021 Census ZCTA data provides information about the shapes and boundaries of different ZCTA's in the United States. It includes the geographic details that help us understand where each ZCTA is located and how it is shaped on a map. You can join this data to additional tables or resources based on the GEOID or ZCTA columns, or spatially join it to other data based on the geometry column. 

A ZCTA is a way to group together a specific set of ZIP codes that share similar characteristics. It's important to note that ZCTAs are not exactly the same as ZIP codes, as they are created by the Census Bureau for statistical purposes rather than for mail delivery. While some ZCTAs may correspond exactly to a single ZIP code, others may represent a combination of multiple ZIP codes or a portion of a larger ZIP code.


|   Column    | Data Type |                     Description                      |
|:-----------:|:--------:|:---------------------------------------------------:|
| ZCTA5CE20   |  Text    | Five-digit ZIP Code Tabulation Area (ZCTA)           |
| GEOID20     |  Text    | Geographic Identifier                               |
| CLASSFP20   |  Text    | Census Class Code                                   |
| MTFCC20     |  Text    | MAF/TIGER Feature Class Code                        |
| FUNCSTAT20  |  Text    | Functional Status of ZCTA                           |
| ALAND20     |  Integer | Land Area (square meters)                           |
| AWATER20    |  Integer | Water Area (square meters)                          |
| INTPTLAT20  |  Decimal | Latitude of the Internal Point                      |
| INTPTLON20  |  Decimal | Longitude of the Internal Point                     |
| geometry    |  Object  | Geospatial representation of the ZCTA polygon shape |


## Notes

- This data has been simplified at a tolerance of 5 meters.
- This data is in the `EPSG:4326` projection. For area or distance calculations, be sure to project it into another coordinate reference system (CRS). For example, area calculations could use the USA Contiguous Albers Equal Area projection (`EPSG:102003`)

## Data Source

This data comes from The [US Census Tiger/Line Geometries](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2021.html#list-tab-790442341).

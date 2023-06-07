# 2019 Counties Geospatial Data (counties.gpkg)

The 2019 Census county data provides information about the shapes and boundaries of different counties in the United States. It includes the geographic details that help us understand where each county is located and how it is shaped on a map. You can join this data to additional tables or resources based on the GEOID column, or spatially join it to other data based on the geometry column. 
## Data Dictionary

| Column Name | Description                                                         | Data Type       |
|-------------|---------------------------------------------------------------------|-----------------|
| REGION      | The region code where the county is located                          | Numeric            |
| DIVISION    | The division code within the region where the county is located      | Numeric            |
| Geo_FIPS    | The Federal Information Processing Standards (FIPS) code             | Text            |
| STATENS     | The unique identifier for the county                                 | Text            |
| GEOID       | The unique identifier for the county within the geographic database. Note that some county GEOID's have leading zeroes.| Text            |
| STUSPS      | The two-letter postal abbreviation for the state                     | Text            |
| Geo_QNAME   | The complete name of the county, including state name                | Text            |
| LSAD        | Legal/Statistical Area Description code indicating county type       | Text            |
| MTFCC       | MAF/TIGER Feature Class Code                                        | Text            |
| FUNCSTAT    | Functional Status code indicating county status                      | Text            |
| ALAND       | Land area in square meters for the county                            | Numeric         |
| AWATER      | Water area in square meters for the county                           | Numeric         |
| INTPTLAT    | Latitude coordinate for the interior point of the county             | Numeric         |
| INTPTLON    | Longitude coordinate for the interior point of the county            | Numeric         |
| geometry    | Geometric representation of the county's boundaries                  | Geometric data type (e.g., Polygon, MultiPolygon) |


## Notes
- This data has been simplified at a tolerance of 5 meters.
- This data is in the `EPSG:4326` projection. For area or distance calculations, be sure to project it into another coordinate reference system (CRS). For example, area calculations could use the USA Contiguous Albers Equal Area projection (`EPSG:102003`)

## Data Source

This data was source from Social Explorer, who redistribute shoreline clipped geographies built from the original TIGER data.
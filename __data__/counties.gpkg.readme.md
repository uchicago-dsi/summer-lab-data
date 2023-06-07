# 2019 Counties Geospatial Data (counties.gpkg)

This geospatial data file

## Data Dictionary

| Column Name | Description                                                         | Data Type       |
|-------------|---------------------------------------------------------------------|-----------------|
| REGION      | The region code where the county is located                          | Text            |
| DIVISION    | The division code within the region where the county is located      | Text            |
| Geo_FIPS    | The Federal Information Processing Standards (FIPS) code             | Text            |
| STATENS     | The unique identifier for the county                                 | Text            |
| GEOID       | The unique identifier for the county within the geographic database | Text            |
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
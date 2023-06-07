# 2021 Counties Geospatial Data (counties.gpkg)

The 2021 Census county data provides information about the shapes and boundaries of different counties in the United States. It includes the geographic details that help us understand where each county is located and how it is shaped on a map. You can join this data to additional tables or resources based on the GEOID column, or spatially join it to other data based on the geometry column.

## Data Dictionary

| Column   | Description                                                                                                            | Data Type       |
| -------- | ---------------------------------------------------------------------------------------------------------------------- | --------------- |
| STATEFP  | Two-digit FIPS code representing the state associated with the county. Note that some codes may have leading zeroes.   | String          |
| COUNTYFP | Three-digit FIPS code representing the county. Note that some codes may have leading zeroes.                           | String          |
| COUNTYNS | Eight-digit FIPS code representing the county. Note that some codes may have leading zeroes.                           | String          |
| GEOID    | Five-digit FIPS code representing the concatenation of state and county. Note that some codes may have leading zeroes. | String          |
| NAME     | Name of the county                                                                                                     | String          |
| NAMELSAD | Name and legal/statistical area description of the county                                                              | String          |
| LSAD     | Legal/statistical area description code for the county                                                                 | String          |
| CLASSFP  | Code representing the county classification                                                                            | String          |
| MTFCC    | MAF/TIGER Feature Class Code for the county                                                                            | String          |
| CSAFP    | Combined Statistical Area FIPS code associated with the county                                                         | String          |
| CBSAFP   | Core Based Statistical Area FIPS code associated with the county                                                       | String          |
| METDIVFP | Metropolitan Division FIPS code associated with the county                                                             | String          |
| FUNCSTAT | Functional status code for the county                                                                                  | String          |
| ALAND    | Land area in square meters for the county                                                                              | Numeric         |
| AWATER   | Water area in square meters for the county                                                                             | Numeric         |
| INTPTLAT | Latitude of the interior point of the county                                                                           | Numeric         |
| INTPTLON | Longitude of the interior point of the county                                                                          | Numeric         |
| geometry | Geometric representation of the county                                                                                 | Geometry object |


## Notes

- This data has been simplified at a tolerance of 5 meters.
- This data is in the `EPSG:4326` projection. For area or distance calculations, be sure to project it into another coordinate reference system (CRS). For example, area calculations could use the USA Contiguous Albers Equal Area projection (`EPSG:102003`)

## Data Source

This data comes from The [US Census Tiger/Line Geometries](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2021.html#list-tab-790442341).

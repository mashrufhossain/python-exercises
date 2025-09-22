"""
Pandas Tutorial 08: How to combine data from multiple tables

This script introduces:
- Concatenating DataFrames row-wise and column-wise
- Using keys to preserve source information
- Merging tables using a common identifier (like SQL joins)
"""

import pandas as pd

# -------------------------------------------------
# 1. Load datasets
# -------------------------------------------------
air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]

print("NO2 data (head):")
print(air_quality_no2.head(), "\n")

print("PM2.5 data (head):")
print(air_quality_pm25.head(), "\n")

# -------------------------------------------------
# 2. Concatenate DataFrames
# -------------------------------------------------
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
print("Concatenated data (head):")
print(air_quality.head(), "\n")

print("Shapes of individual and combined tables:")
print("air_quality_pm25:", air_quality_pm25.shape)
print("air_quality_no2 :", air_quality_no2.shape)
print("combined        :", air_quality.shape, "\n")

# Sort by datetime
air_quality = air_quality.sort_values("date.utc")
print("Concatenated & sorted by date:")
print(air_quality.head(), "\n")

# Concatenate with keys → MultiIndex
air_quality_multi = pd.concat(
    [air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"]
)
print("Concatenated with hierarchical keys (head):")
print(air_quality_multi.head(), "\n")

# -------------------------------------------------
# 3. Merge with station coordinates
# -------------------------------------------------
stations_coord = pd.read_csv("data/air_quality_stations.csv")
print("Stations metadata:")
print(stations_coord.head(), "\n")

air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
print("Merged air quality with station coordinates:")
print(air_quality.head(), "\n")

# -------------------------------------------------
# 4. Merge with parameter descriptions
# -------------------------------------------------
air_quality_params = pd.read_csv("data/air_quality_parameters.csv")
print("Parameters metadata:")
print(air_quality_params.head(), "\n")

air_quality = pd.merge(
    air_quality,
    air_quality_params,
    how="left",
    left_on="parameter",
    right_on="id",
)
print("Merged air quality with parameter descriptions:")
print(air_quality.head(), "\n")

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- Use pd.concat() to stack DataFrames row-wise or column-wise")
print("- Use keys in concat() to track data source (MultiIndex)")
print("- Use pd.merge() for database-style joins")
print("- left_on/right_on can link different column names across tables")

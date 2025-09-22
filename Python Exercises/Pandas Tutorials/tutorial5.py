"""
Pandas Tutorial 05: How to create new columns derived from existing columns

This script introduces:
- Creating new columns with element-wise operations
- Using mathematical and logical operators
- Renaming columns with dictionaries or functions
"""

import pandas as pd

# -------------------------------------------------
# 1. Load Air Quality dataset
# -------------------------------------------------
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
print("First rows of air quality dataset:")
print(air_quality.head(), "\n")

# -------------------------------------------------
# 2. Create a new column with unit conversion
# -------------------------------------------------
# Conversion factor: 1 µg/m³ → 1.882 mg/m³ (assumed conditions: 25°C, 1013 hPa)
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
print("Data with new column (London concentration in mg/m³):")
print(air_quality.head(), "\n")

# -------------------------------------------------
# 3. Calculate a ratio column (Paris vs Antwerp)
# -------------------------------------------------
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)
print("Data with ratio column (Paris/Antwerp):")
print(air_quality.head(), "\n")

# -------------------------------------------------
# 4. Rename columns with a dictionary
# -------------------------------------------------
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
print("Data with renamed columns:")
print(air_quality_renamed.head(), "\n")

# -------------------------------------------------
# 5. Rename columns using a function (convert to lowercase)
# -------------------------------------------------
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print("Data with lowercase column names:")
print(air_quality_renamed.head(), "\n")

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- Create new columns with [] and assignment")
print("- Operations are element-wise, no need for loops")
print("- Use .rename() with dict or function to update row/column labels")

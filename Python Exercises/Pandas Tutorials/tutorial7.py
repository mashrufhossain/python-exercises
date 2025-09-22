"""
Pandas Tutorial 07: How to reshape the layout of tables

This script introduces:
- Sorting rows by one or multiple columns
- Converting long ↔ wide table formats with pivot, pivot_table, and melt
"""

import pandas as pd

# -------------------------------------------------
# 1. Load Titanic dataset
# -------------------------------------------------
titanic = pd.read_csv("data/titanic.csv")
print("First 5 rows of Titanic dataset:")
print(titanic.head(), "\n")

# Sort by Age
print("Passengers sorted by Age:")
print(titanic.sort_values(by="Age").head(), "\n")

# Sort by Pclass and Age (descending)
print("Passengers sorted by Pclass and Age (descending):")
print(titanic.sort_values(by=["Pclass", "Age"], ascending=False).head(), "\n")

# -------------------------------------------------
# 2. Load Air Quality dataset
# -------------------------------------------------
air_quality = pd.read_csv(
    "data/air_quality_long.csv", index_col="date.utc", parse_dates=True
)
print("First 5 rows of Air Quality dataset:")
print(air_quality.head(), "\n")

# -------------------------------------------------
# 3. Long → Wide (pivot)
# -------------------------------------------------
# Filter NO2 measurements
no2 = air_quality[air_quality["parameter"] == "no2"]

# Keep first 2 measurements per location
no2_subset = no2.sort_index().groupby("location").head(2)
print("Subset of NO2 data (first 2 per location):")
print(no2_subset, "\n")

# Pivot to wide format
print("Pivoted NO2 data (wide format):")
print(no2_subset.pivot(columns="location", values="value"), "\n")

# Example for plotting (commented for script mode):
# no2.pivot(columns="location", values="value").plot()

# -------------------------------------------------
# 4. Pivot table (aggregation)
# -------------------------------------------------
print("Pivot table: mean concentration by station and parameter:")
print(
    air_quality.pivot_table(
        values="value", index="location", columns="parameter", aggfunc="mean"
    ),
    "\n",
)

print("Pivot table with margins (subtotals):")
print(
    air_quality.pivot_table(
        values="value",
        index="location",
        columns="parameter",
        aggfunc="mean",
        margins=True,
    ),
    "\n",
)

# Equivalent with groupby
print("Equivalent groupby result:")
print(air_quality.groupby(["parameter", "location"])[["value"]].mean(), "\n")

# -------------------------------------------------
# 5. Wide → Long (melt)
# -------------------------------------------------
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
print("Pivoted NO2 data with reset index:")
print(no2_pivoted.head(), "\n")

# Melt to long format
no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)
print("Melted NO2 data (long format):")
print(no_2.head(), "\n")

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- sort_values sorts rows by one or more columns")
print("- pivot reshapes without aggregation (requires unique index/column pairs)")
print("- pivot_table reshapes with aggregation (like Excel pivot tables)")
print("- melt converts wide format back to long format")

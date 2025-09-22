"""
Pandas Tutorial 09: How to handle time series data with ease

This script introduces:
- Converting strings to datetime objects
- Using datetime properties via .dt accessor
- Grouping by datetime components (weekday, hour, etc.)
- Using a DatetimeIndex for slicing and resampling
"""

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Load and prepare dataset
# -------------------------------------------------
air_quality = pd.read_csv("data/air_quality_no2_long.csv")
air_quality = air_quality.rename(columns={"date.utc": "datetime"})

print("Head of raw data:")
print(air_quality.head(), "\n")

# Convert datetime column to pandas datetime type
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])

# -------------------------------------------------
# 2. Basic datetime operations
# -------------------------------------------------
print("Start and end date of dataset:")
print(air_quality["datetime"].min(), air_quality["datetime"].max(), "\n")

print("Length of time series (Timedelta):")
print(air_quality["datetime"].max() - air_quality["datetime"].min(), "\n")

# Add month column
air_quality["month"] = air_quality["datetime"].dt.month
print("With new 'month' column:")
print(air_quality.head(), "\n")

# -------------------------------------------------
# 3. Grouping by datetime properties
# -------------------------------------------------
print("Average NO2 per weekday per location:")
weekday_means = air_quality.groupby(
    [air_quality["datetime"].dt.weekday, "location"]
)["value"].mean()
print(weekday_means, "\n")

# Average value per hour of day
print("Average NO2 per hour of the day (all stations):")
hourly_means = air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean()
print(hourly_means, "\n")

# Plot hourly pattern
fig, axs = plt.subplots(figsize=(12, 4))
hourly_means.plot(kind="bar", rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
plt.title("Average hourly NO2 concentration")
plt.tight_layout()
plt.show()

# -------------------------------------------------
# 4. Datetime as index
# -------------------------------------------------
no2 = air_quality.pivot(index="datetime", columns="location", values="value")
print("Pivoted NO2 data (wide format):")
print(no2.head(), "\n")

print("Index year and weekday properties:")
print(no2.index.year[:5], no2.index.weekday[:5], "\n")

# Subset by date range
print("Subset from 2019-05-20 to 2019-05-21:")
print(no2["2019-05-20":"2019-05-21"].head(), "\n")

no2["2019-05-20":"2019-05-21"].plot(title="NO2 on May 20–21, 2019")
plt.ylabel("$NO_2 (µg/m^3)$")
plt.tight_layout()
plt.show()

# -------------------------------------------------
# 5. Resampling time series
# -------------------------------------------------
# Monthly maximum values
monthly_max = no2.resample("ME").max()
print("Monthly maximum NO2 values:")
print(monthly_max, "\n")

print("Frequency of resampled index:", monthly_max.index.freq, "\n")

# Plot daily mean
no2.resample("D").mean().plot(style="-o", figsize=(10, 5))
plt.title("Daily mean NO2 concentrations")
plt.ylabel("$NO_2 (µg/m^3)$")
plt.tight_layout()
plt.show()

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- Use pd.to_datetime() to convert strings to datetime")
print("- Use .dt accessor for datetime properties")
print("- A DatetimeIndex supports slicing and time-based operations")
print("- Use resample() to change time series frequency with aggregation")

"""
Pandas Tutorial 04: How do I create plots in pandas?

This script introduces:
- Quick plots from DataFrames and Series
- Scatter plots to compare columns
- Boxplots and other plot types
- Subplots for multiple columns
- Customizing and saving plots using Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Load Air Quality dataset
# -------------------------------------------------
# (Make sure "data/air_quality_no2.csv" exists in your repo before running this.)
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
print("First rows of air quality dataset:")
print(air_quality.head(), "\n")

# -------------------------------------------------
# 2. Quick visual check of the data
# -------------------------------------------------
air_quality.plot()
plt.title("Air Quality (Line Plot of All Stations)")
plt.show()

# -------------------------------------------------
# 3. Plot a single column (Paris station)
# -------------------------------------------------
air_quality["station_paris"].plot()
plt.title("Air Quality in Paris (Line Plot)")
plt.show()

# -------------------------------------------------
# 4. Scatter plot: London vs Paris
# -------------------------------------------------
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.title("Scatter Plot: London vs Paris NO2 Levels")
plt.show()

# -------------------------------------------------
# 5. Boxplot
# -------------------------------------------------
air_quality.plot.box()
plt.title("Boxplot of NO2 Concentrations by Station")
plt.show()

# -------------------------------------------------
# 6. Area plots with subplots
# -------------------------------------------------
air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.suptitle("Area Plots for Each Station (Subplots)")
plt.show()

# -------------------------------------------------
# 7. Customizing plots with Matplotlib
# -------------------------------------------------
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)  # pandas plotting onto custom Axes
axs.set_ylabel("NO$_2$ concentration")
axs.set_title("Customized Area Plot of NO2 Concentrations")
fig.savefig("no2_concentrations.png")  # Save to file
plt.show()

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- Use .plot.* methods on DataFrames or Series")
print("- Default plot is line; alternatives include scatter, box, hist, area, etc.")
print("- subplots=True gives separate plots per column")
print("- All pandas plots are Matplotlib objects → you can customize & save them")

"""
Pandas Tutorial 06: How to calculate summary statistics

This script introduces:
- Aggregating statistics (mean, median, describe, agg)
- Grouped statistics with groupby (split-apply-combine)
- Counting records by category with value_counts
"""

import pandas as pd

# -------------------------------------------------
# 1. Load Titanic dataset
# -------------------------------------------------
titanic = pd.read_csv("data/titanic.csv")
print("First 5 rows of Titanic dataset:")
print(titanic.head(), "\n")

# -------------------------------------------------
# 2. Aggregating statistics
# -------------------------------------------------
# Average age
avg_age = titanic["Age"].mean()
print("Average age of Titanic passengers:", avg_age, "\n")

# Median age and fare
print("Median age and fare:")
print(titanic[["Age", "Fare"]].median(), "\n")

# Describe summary
print("Summary statistics for Age and Fare:")
print(titanic[["Age", "Fare"]].describe(), "\n")

# Multiple aggregations with .agg()
print("Custom aggregations with .agg():")
print(
    titanic.agg(
        {
            "Age": ["min", "max", "median", "skew"],
            "Fare": ["min", "max", "median", "mean"],
        }
    ),
    "\n",
)

# -------------------------------------------------
# 3. Grouped statistics
# -------------------------------------------------
# Average age by sex
print("Average age by sex:")
print(titanic[["Sex", "Age"]].groupby("Sex").mean(), "\n")

# Groupby on all numeric columns
print("Mean of numeric columns grouped by sex:")
print(titanic.groupby("Sex").mean(numeric_only=True), "\n")

# Groupby with selection
print("Average age by sex (selected column):")
print(titanic.groupby("Sex")["Age"].mean(), "\n")

# Grouping by multiple columns
print("Mean fare by sex and passenger class:")
print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean(), "\n")

# -------------------------------------------------
# 4. Count records by category
# -------------------------------------------------
print("Number of passengers in each cabin class (value_counts):")
print(titanic["Pclass"].value_counts(), "\n")

print("Equivalent with groupby + count:")
print(titanic.groupby("Pclass")["Pclass"].count(), "\n")

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- Aggregations work column-wise, missing values excluded by default")
print("- groupby uses the split-apply-combine pattern")
print("- value_counts is a quick way to count category frequencies")

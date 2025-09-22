"""
Pandas Tutorial 03: How do I select a subset of a DataFrame?

This script introduces:
- Selecting specific columns
- Filtering rows based on conditions
- Handling missing values
- Using loc and iloc for combined row/column selection
- Assigning new values to subsets
"""

import pandas as pd

# -------------------------------------------------
# 1. Load Titanic dataset
# -------------------------------------------------
titanic = pd.read_csv("data/titanic.csv")
print("First 5 rows of Titanic dataset:")
print(titanic.head(), "\n")

# -------------------------------------------------
# 2. Select specific columns
# -------------------------------------------------
# Single column → Series
ages = titanic["Age"]
print("Age column as Series:")
print(ages.head(), "\n")
print("Type:", type(ages))
print("Shape:", titanic["Age"].shape, "\n")

# Multiple columns → DataFrame
age_sex = titanic[["Age", "Sex"]]
print("Age & Sex columns:")
print(age_sex.head(), "\n")
print("Type:", type(age_sex))
print("Shape:", age_sex.shape, "\n")

# -------------------------------------------------
# 3. Filter rows
# -------------------------------------------------
# Passengers older than 35
above_35 = titanic[titanic["Age"] > 35]
print("Passengers older than 35:")
print(above_35.head(), "\n")
print("Shape:", above_35.shape, "\n")

# Passengers from cabin class 2 or 3
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print("Passengers in classes 2 or 3:")
print(class_23.head(), "\n")

# Equivalent with OR operator
class_23_or = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print("Equivalent OR filter (classes 2 or 3):")
print(class_23_or.head(), "\n")

# Passengers with known age
age_no_na = titanic[titanic["Age"].notna()]
print("Passengers with known Age:")
print(age_no_na.head(), "\n")
print("Shape:", age_no_na.shape, "\n")

# -------------------------------------------------
# 4. Select both rows & columns with loc
# -------------------------------------------------
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print("Names of passengers older than 35:")
print(adult_names.head(), "\n")

# -------------------------------------------------
# 5. Select by row/column positions with iloc
# -------------------------------------------------
rows_10_to_25_cols_3_to_5 = titanic.iloc[9:25, 2:5]
print("Rows 10-25 and columns 3-5:")
print(rows_10_to_25_cols_3_to_5, "\n")

# -------------------------------------------------
# 6. Assign new values using iloc
# -------------------------------------------------
titanic.iloc[0:3, 3] = "anonymous"  # overwrite first 3 names
print("Modified first 3 names in column 'Name':")
print(titanic.head(), "\n")

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- Use [] for subsets (columns, lists, slices, or conditions)")
print("- Use loc for selection by labels (rows/columns)")
print("- Use iloc for selection by positions (rows/columns)")
print("- You can assign new values to subsets with loc/iloc")

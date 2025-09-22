"""
Pandas Tutorial 02: How do I read and write tabular data?

This script introduces:
- Reading CSV and Excel files into pandas
- Inspecting data with head(), tail(), dtypes, and info()
- Exporting data to Excel
"""

import pandas as pd

# -------------------------------------------------
# 1. Read data from a CSV file
# -------------------------------------------------
# (Make sure "data/titanic.csv" exists in your repo before running this.)
titanic = pd.read_csv("data/titanic.csv")

print("Titanic DataFrame (first 5 rows by default):")
print(titanic, "\n")   # By default shows head and tail

# -------------------------------------------------
# 2. View first N rows of the DataFrame
# -------------------------------------------------
print("First 8 rows of Titanic dataset:")
print(titanic.head(8), "\n")

# Want last N rows instead?
# print(titanic.tail(10))

# -------------------------------------------------
# 3. Inspect column data types
# -------------------------------------------------
print("Column data types:")
print(titanic.dtypes, "\n")

# -------------------------------------------------
# 4. Write DataFrame to Excel
# -------------------------------------------------
# Store as Excel file with custom sheet name, without the index
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
print("Data exported to 'titanic.xlsx' (sheet name: passengers).")

# -------------------------------------------------
# 5. Read Excel file back into pandas
# -------------------------------------------------
titanic_from_excel = pd.read_excel("titanic.xlsx", sheet_name="passengers")
print("DataFrame read back from Excel:")
print(titanic_from_excel.head(), "\n")

# -------------------------------------------------
# 6. Get technical summary of the DataFrame
# -------------------------------------------------
print("Technical summary of Titanic dataset:")
titanic.info()

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("\nREMEMBER:")
print("- Use read_* functions (e.g., read_csv, read_excel) to import data")
print("- Use to_* methods (e.g., to_excel, to_csv) to export data")
print("- head(), tail(), dtypes, and info() are useful for quick checks")

"""
Pandas Tutorial 10: How to manipulate textual data

This script introduces:
- Using .str accessor for element-wise string methods
- Extracting parts of strings (splitting, indexing)
- Filtering rows with string matching
- Measuring string lengths
- Replacing values with mappings
"""

import pandas as pd

# -------------------------------------------------
# 1. Load dataset
# -------------------------------------------------
titanic = pd.read_csv("data/titanic.csv")

print("Head of Titanic dataset:")
print(titanic.head(), "\n")

# -------------------------------------------------
# 2. String transformations
# -------------------------------------------------
print("Convert all names to lowercase:")
print(titanic["Name"].str.lower().head(), "\n")

# Extract surname (text before comma)
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
print("Extracted Surnames:")
print(titanic["Surname"].head(), "\n")

# -------------------------------------------------
# 3. Conditional string filtering
# -------------------------------------------------
print("Passenger(s) with 'Countess' in their name:")
print(titanic[titanic["Name"].str.contains("Countess")], "\n")

# -------------------------------------------------
# 4. String length analysis
# -------------------------------------------------
# Find the passenger with the longest name
longest_name_index = titanic["Name"].str.len().idxmax()
longest_name = titanic.loc[longest_name_index, "Name"]

print("Passenger with the longest name:")
print(f"Index: {longest_name_index}, Name: {longest_name}\n")

# -------------------------------------------------
# 5. Value replacement
# -------------------------------------------------
# Replace 'male' -> 'M', 'female' -> 'F'
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
print("Sex column with shorthand values:")
print(titanic[["Sex", "Sex_short"]].head(), "\n")

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- Use .str accessor for element-wise string operations")
print("- Combine string methods like .split() and .get() to extract parts")
print("- Use .contains() for filtering rows with string conditions")
print("- Use .len() and idxmax() to find the longest text values")
print("- Use replace() with a mapping dict for clean value translation")

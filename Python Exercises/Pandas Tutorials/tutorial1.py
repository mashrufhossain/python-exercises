"""
Pandas Tutorial 01: What kind of data does pandas handle?

This script introduces:
- Importing pandas
- Creating a DataFrame from a dictionary
- Accessing columns (Series)
- Performing basic operations
"""

import pandas as pd

# -------------------------------------------------
# 1. Create a DataFrame manually
# -------------------------------------------------
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print("Full DataFrame:")
print(df, "\n")

# -------------------------------------------------
# 2. Access a single column (as a Series)
# -------------------------------------------------
ages = df["Age"]
print("Age column as Series:")
print(ages, "\n")

# Or create a Series directly
ages_direct = pd.Series([22, 35, 58], name="Age")
print("Series created directly:")
print(ages_direct, "\n")

# -------------------------------------------------
# 3. Do something with a Series or DataFrame
# -------------------------------------------------
print("Maximum Age (from DataFrame):", df["Age"].max())
print("Maximum Age (from Series):", ages.max(), "\n")

# -------------------------------------------------
# 4. Basic statistics
# -------------------------------------------------
print("Basic statistics of numerical data:")
print(df.describe(), "\n")

# -------------------------------------------------
# Summary reminder
# -------------------------------------------------
print("REMEMBER:")
print("- Import pandas as pd")
print("- Use DataFrame to store tabular data")
print("- Each column in a DataFrame is a Series")
print("- Apply methods to DataFrames/Series for calculations")

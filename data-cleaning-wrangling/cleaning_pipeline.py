import pandas as pd
import numpy as np

"""
Purpose:
Clean and standardize raw sales data to ensure accurate reporting and analysis.

Key Cleaning Steps:
- Normalize category labels
- Fix inconsistent date formats
- Remove duplicate records
- Handle missing profit values
"""

df = pd.read_csv("raw/superstore.csv")

# Normalize category labels
df['Category'] = df['Category'].str.strip().str.title()

# Fix broken dates
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing profit
df['Profit'] = df['Profit'].fillna(0)

# Save cleaned data
df.to_csv("cleaned/superstore_cleaned.csv", index=False)

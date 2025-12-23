import numpy as np

df = pd.read_csv("raw/superstore.csv")

# Normalize category labels
df['Category'] = df['Category'].str.strip().str.title()

# Fix broken dates
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing profit
df['Profit'] = df['Profit'].fillna(0)


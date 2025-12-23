import pandas as pd

df = pd.read_csv("data/raw/online_retail.csv")

# Remove canceled orders
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Handle missing customers
df = df.dropna(subset=['CustomerID'])

# Create revenue metric
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Convert date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df.to_csv("data/cleaned/cleaned_sales.csv", index=False)


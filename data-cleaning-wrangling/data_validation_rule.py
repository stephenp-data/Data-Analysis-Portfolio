import pandas as pd

"""
Purpose:
Validate cleaned sales data to ensure it meets basic business rules
before analysis or reporting.
"""

df = pd.read_csv("cleaned/superstore_cleaned.csv")

# Business rule: sales values should never be negative
assert (df['Sales'] >= 0).all(), "Negative sales detected!"


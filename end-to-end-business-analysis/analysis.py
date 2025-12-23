import pandas as pd

"""
Purpose:
Analyze monthly revenue trends and calculate month-over-month growth
to identify business performance patterns.
"""

df = pd.read_csv("data/cleaned/cleaned_sales.csv")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

monthly_revenue = (
    df
    .set_index('InvoiceDate')
    .resample('M')['Revenue']
    .sum()
)

growth_rate = monthly_revenue.pct_change() * 100

print(monthly_revenue.head())
print(growth_rate.head())

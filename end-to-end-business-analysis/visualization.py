import pandas as pd
import matplotlib.pyplot as plt

"""
Purpose:
Visualize monthly revenue trends to support business performance reporting.
"""

df = pd.read_csv("data/cleaned/cleaned_sales.csv")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

monthly_revenue = (
    df
    .set_index('InvoiceDate')
    .resample('M')['Revenue']
    .sum()
)

monthly_revenue.plot(figsize=(10,5), title="Monthly Revenue Trend")
plt.ylabel("Revenue (£)")
plt.xlabel("Month")
plt.tight_layout()
plt.show()

import pandas as pd

"""
Purpose:
Calculate the overall customer churn rate for a subscription business.
This KPI helps quantify the percentage of customers lost during the period.
"""

df = pd.read_csv("data/telco_churn.csv")

churn_rate = (
    df['Churn']
    .value_counts(normalize=True)
    .loc['Yes'] * 100
)

print(f"Overall churn rate: {churn_rate:.2f}%")

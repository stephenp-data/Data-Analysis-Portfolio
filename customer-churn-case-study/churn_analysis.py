import pandas as pd

"""
Purpose:
Analyze churn rate by contract type to identify high-risk customer segments.
"""

df = pd.read_csv("data/telco_churn.csv")

churn_by_contract = (
    df.groupby('Contract')['Churn']
    .apply(lambda x: (x == 'Yes').mean() * 100)
)

print(churn_by_contract)


"""
Insight:
Month-to-month contracts show significantly higher churn,
suggesting an opportunity for long-term contract incentives.
"""

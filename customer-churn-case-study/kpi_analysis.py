df = pd.read_csv("data/telco_churn.csv")

churn_rate = (
    df['Churn']
    .value_counts(normalize=True)
    .loc['Yes'] * 100
)

print(f"Overall churn rate: {churn_rate:.2f}%")


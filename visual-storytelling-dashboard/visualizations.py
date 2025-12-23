import seaborn as sns

region_sales = (
    df.groupby('Region')['Sales']
    .sum()
    .sort_values(ascending=False)
)

sns.barplot(
    x=region_sales.values,
    y=region_sales.index
)


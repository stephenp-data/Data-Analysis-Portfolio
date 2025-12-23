
monthly_revenue = (
    df
    .set_index('InvoiceDate')
    .resample('M')['Revenue']
    .sum()
)

growth_rate = monthly_revenue.pct_change() * 100

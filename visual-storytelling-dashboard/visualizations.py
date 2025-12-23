import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
Purpose:
Visualize regional sales performance to support executive-level
decision making and storytelling.
"""

df = pd.read_csv("data/global_superstore.csv")

region_sales = (
    df.groupby('Region')['Sales']
    .sum()
    .sort_values(ascending=False)
)

sns.barplot(
    x=region_sales.values,
    y=region_sales.index
)

plt.title("Total Sales by Region")
plt.xlabel("Sales")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)

plt.style.use('seaborn-v0_8')

num_rows = 100

data = {
    "Order_Date":pd.date_range(start="2025-01-01",periods=num_rows,freq="D"),
    "Product_Category":np.random.choice(['Electronics', 'Clothing', 'Furniture', 'Toys', 'Books'],num_rows),
    "Revenue":np.random.randint(100,5000,num_rows),
    "Regions":np.random.choice(['North', 'South', 'East', 'West'],num_rows)
}

df = pd.DataFrame(data)
df["Order_Date"] = pd.to_datetime(df['Order_Date'])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

monthly_revenue = df.groupby("Month")["Revenue"].sum()

revenue_by_category = df.groupby("Product_Category")["Revenue"].sum()

revenue_by_regions = df.groupby("Regions")["Revenue"].sum()

heatmap_data = pd.pivot_table(df,values="Revenue",index="Product_Category",columns="Regions",aggfunc="sum")

fig, axes = plt.subplots(3, 2, figsize=(15, 15))
fig.tight_layout(pad=5.0)

axes[0,0].plot(monthly_revenue.index,monthly_revenue.values,marker="o",color="salmon")
axes[0,0].set_title("Monthly Revenue Trend")
axes[0,0].set_xlabel("Months")
axes[0,0].set_ylabel("Revenues")

axes[0,1].bar(revenue_by_category.index,revenue_by_category.values,color="teal")
axes[0,1].set_title("Revenue By Products")
axes[0,1].set_ylabel("Revenue")

axes[1,0].pie(revenue_by_regions.values,labels=revenue_by_regions.index,autopct='%1.1f%%',colors=sns.color_palette("pastel"))
axes[1,0].set_title("Revenue distribution by regions")

sns.heatmap(heatmap_data,annot=True, fmt='.0f', cmap='YlGnBu', ax=axes[1, 1])
axes[1,1].set_title("Revenue by category and region")

sns.boxplot(data=df, x='Product_Category', y='Revenue', ax=axes[2, 0], palette='Set2')
axes[2, 0].set_title('Revenue Distribution per Category')
axes[2, 0].tick_params(axis='x', rotation=45)

# Hide last empty subplot
axes[2, 1].axis('off')

plt.show()
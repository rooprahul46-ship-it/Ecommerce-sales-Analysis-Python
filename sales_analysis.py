import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("sales_data.csv")

# Data Cleaning
df.drop_duplicates(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]
df["Month"] = df["Date"].dt.strftime("%Y-%m")
df["Day"] = df["Date"].dt.day_name()

# KPIs
total_revenue = df["Revenue"].sum()
total_orders = df["Order_ID"].nunique()
avg_order_value = round(total_revenue / total_orders, 2)
best_city = df.groupby("City")["Revenue"].sum().idxmax()
best_category = df.groupby("Category")["Revenue"].sum().idxmax()

print("========== BUSINESS KPI DASHBOARD ==========")
print("Total Revenue      :", total_revenue)
print("Total Orders       :", total_orders)
print("Avg Order Value    :", avg_order_value)
print("Top Performing City:", best_city)
print("Best Category      :", best_category)

# Top 5 Customers
print("\n===== TOP CUSTOMERS =====")
print(df.groupby("Customer")["Revenue"].sum().sort_values(ascending=False).head(5))

# Monthly Trend
monthly = df.groupby("Month")["Revenue"].sum()

# Product Performance
products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10)

# Charts
plt.figure(figsize=(10,5))
monthly.plot(marker="o", linewidth=3)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
df.groupby("Category")["Revenue"].sum().plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,8))
df.groupby("City")["Revenue"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("City Revenue Share")
plt.ylabel("")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
products.plot(kind="barh")
plt.title("Top Products by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.show()
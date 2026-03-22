import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
data = pd.read_csv("ecommerce_sales_data.csv")

print("First 5 rows of dataset:")
print(data.head())

print("\nColumn names:")
print(data.columns)

print("\nDataset info:")
print(data.info())

print("\nStatistical summary:")
print(data.describe())

# 2. Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# 3. Create Total Sales column (using Revenue from the new dataset)
if "Total" not in data.columns:
    data["Total"] = data["Revenue"]

# 4. Total Revenue
total_revenue = data["Total"].sum()
print("\nTotal Revenue:", total_revenue)

# 5. Best Selling Category (New dataset uses Units_Sold and Category instead of Quantity and Product)
best_category = data.groupby("Category")["Units_Sold"].sum().idxmax()
print("Best Selling Category:", best_category)

# 6. Top Revenue Category
top_revenue_category = data.groupby("Category")["Total"].sum().idxmax()
print("Top Revenue Category:", top_revenue_category)

# 7. Sales by Category
category_sales = data.groupby("Category")["Total"].sum()
print("\nSales by Category:")
print(category_sales)

# 8. Sort month string column logically
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
data["Month"] = pd.Categorical(data["Month"], categories=months, ordered=True)

# 9. Monthly Sales Analysis
monthly_sales = data.groupby("Month", observed=False)["Total"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# 10. Visualization - Monthly Sales Chart
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales (Revenue)")
plt.show()
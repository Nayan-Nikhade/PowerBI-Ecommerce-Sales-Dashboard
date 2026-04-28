import sqlite3
import pandas as pd

conn = sqlite3.connect('retail.db')

print("=== KEY BUSINESS METRICS ===")

# 1. Net Revenue 
revenue = pd.read_sql("SELECT ROUND(SUM(TotalPrice),2) as Net_Revenue FROM retail", conn)
print("\n1. Net Revenue: £", revenue['Net_Revenue'][0])

# 2. Top 10 Products
print("\n2. Top 10 Products by Revenue:")
top10 = pd.read_sql("""
SELECT Description, ROUND(SUM(TotalPrice),2) as Revenue 
FROM retail 
GROUP BY StockCode, Description 
ORDER BY Revenue DESC LIMIT 10
""", conn)
print(top10)

# 3. Revenue by Country 
print("\n3. Revenue by Country:")
country = pd.read_sql("""
SELECT Country, ROUND(SUM(TotalPrice),2) as Revenue,
ROUND(SUM(TotalPrice) * 100.0 / (SELECT SUM(TotalPrice) FROM retail), 1) as Percent
FROM retail GROUP BY Country ORDER BY Revenue DESC LIMIT 5
""", conn)
print(country)

# 4. Data Quality Note
total_rows = pd.read_sql("SELECT COUNT(*) as count FROM retail", conn)
print(f"\n4. Total Cleaned Transactions Analyzed: {total_rows['count'][0]:,}")

conn.close()
print("\n=== DONE ===")

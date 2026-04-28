import pandas as pd
import sqlite3

print("Loading...")
df = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011')
print("Original rows:", len(df))

df = df[df['Quantity'] > 0]
df = df[df['Price'] > 0] 
df = df.dropna(subset=['Customer ID'])
df['Customer ID'] = df['Customer ID'].astype(int)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalPrice'] = df['Quantity'] * df['Price']

print("Cleaned rows:", len(df))

conn = sqlite3.connect('retail.db')
df.to_sql('retail', conn, if_exists='replace', index=False)
conn.close()
df.to_csv('cleaned_retail.csv', index=False)
print("Done. Files saved.")

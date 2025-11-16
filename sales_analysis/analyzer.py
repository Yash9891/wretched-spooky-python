# import os

# # check if we are in the right place
# print("current directory:", os.getcwd())

# # check if our data file exists
# # data_path = '../codespaces-flask/Array.py'   -----  ../ is use to go a level up fromt the current folder


# data_path = 'sales_analysis/data/sales.csv'

# if os.path.exists(data_path):
#     print(f'Found {data_path}')
# else:
#     print(f'Cannot find {data_path}')
#     print("Make sure you are running from the sales analysis folder")


# Pandas----------------------------------------
# import pandas as pd
# import json
# import os

# # Read the CSV file
# df = pd.read_csv('sales_analysis/data/sales.csv')
# print("CSV Data:")
# print(df)
# print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# # Quick operation: calculate total for each row
# df['total'] = df['quantity'] * df['price']
# print("\nWith totals:")
# print(df)

# # Create output directory
# os.makedirs('sales_analysis/output', exist_ok=True)

# # Save as different formats

# # 1. JSON format (good for web APIs)
# df.to_json('sales_analysis/output/sales_data.json', orient='records', indent=2)

# # 2. Excel format (good for sharing)
# df.to_excel('sales_analysis/output/sales_data.xlsx', index=False)

# # 3. Updated CSV (with our new total column)
# df.to_csv('sales_analysis/output/sales_with_totals.csv', index=False)

# print("\nFiles saved:")
# print("- output/sales_data.json")
# print("- output/sales_data.xlsx")
# print("- output/sales_with_totals.csv")




#Using helper functions ----------------------------------------------------
import pandas as pd
from helpers import calculate_total, format_currency

# Read data
df = pd.read_csv('sales_analysis/data/sales.csv')

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

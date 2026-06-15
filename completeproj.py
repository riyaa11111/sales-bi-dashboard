# import pandas as pd
# import matplotlib.pyplot as plt
# import datetime as dt
#
# # Load the file
# df = pd.read_csv(r"C:\Users\riyaj\OneDrive\Desktop\salesdata.csv")
# pd.set_option('display.max_columns', None)
#
# # --- OVERWRITE COLUMNS BY POSITION ---
# df.columns = ['Order id', 'Product', 'Quantities Ordered', 'Price Each', 'Order date', 'Purchase address']
#
# df.dropna(inplace=True)
#
# # FIXED: Explicitly defined the format to match the "DD-MM-YYYY HH.MM" structure in your CSV
# df['Order date'] = pd.to_datetime(df['Order date'], format='%d-%m-%Y %H.%M')
# df['Month'] = df['Order date'].dt.month
#
# df['Sales'] = df['Quantities Ordered'] * df['Price Each']
#
# # Define sales targets
# sales_targets = {
#     'USB-C Charging Cable': 2000,
#     'Bose SoundSport': 1500,
#     'AAA Batteries (4-pack)': 1000,
#     'Google Phone': 5000,
#     'Macbook Pro Laptop': 8000,
#     'Wired Headphones': 1500
# }
#
# # Calculate total sales per product
# product_sales = df.groupby('Product')['Sales'].sum().reset_index()
#
# # Evaluate performance against targets
# product_sales['Target'] = product_sales['Product'].map(sales_targets).fillna(0)
# product_sales['Performance'] = product_sales['Sales'] - product_sales['Target']
#
# # Visualization
# plt.figure(figsize=(10, 6))
#
# plt.bar(product_sales['Product'], product_sales['Sales'], label='Actual sales', color='r')
# plt.bar(product_sales['Product'], product_sales['Target'], label='Target sales', alpha=0.5, color='blue')
#
# plt.xlabel('Product')
# plt.ylabel('Sales')
# plt.title('Actual vs Target Sales by Product')
#
# plt.xticks(rotation=45, ha='right')
# plt.legend()
# plt.tight_layout()
#
# plt.show()
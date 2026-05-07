import pandas as pd

orders = pd.read_csv('olist_orders_dataset.csv')
items = pd.read_csv('olist_order_items_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')
customers = pd.read_csv('olist_customers_dataset.csv')

df = items.merge(orders, on='order_id')
df = df.merge(products, on='product_id')
df = df.merge(customers, on='customer_id')

df = df.dropna()

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

df['ano'] = df['order_purchase_timestamp'].dt.year
df['mes'] = df['order_purchase_timestamp'].dt.month

df.to_csv('dados_tratados.csv', index=False)

print("Arquivo criado com sucesso!") 
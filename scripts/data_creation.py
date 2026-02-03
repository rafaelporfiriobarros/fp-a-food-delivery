# Bibliotecas

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parâmetros globais

np.random.seed(42)
N_ORDERS = 100_000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 3, 31)

# Dimensões

cities = {
    "São Paulo": {"region": "Sudeste", "courier_index": 1.20},
    "Rio de Janeiro": {"region": "Sudeste", "courier_index": 1.15},
    "Belo Horizonte": {"region": "Sudeste", "courier_index": 1.05},
    "Curitiba": {"region": "Sul", "courier_index": 1.00},
    "Porto Alegre": {"region": "Sul", "courier_index": 1.10},
}

df_cities = (
    pd.DataFrame.from_dict(cities, orient="index")
    .reset_index()
    .rename(columns={
        "index": "city",
        "courier_index": "courier_cost_index"
    })
)


categories = {
    "Hamburguer": 0.27,
    "Pizza": 0.25,
    "Japonesa": 0.30,
    "Brasileira": 0.23,
    "Saudável": 0.28,
}

# Restaurantes

restaurants = []

for i in range(1, 201):
    city = np.random.choice(list(cities.keys()))
    category = np.random.choice(list(categories.keys()))
    restaurants.append({
        "restaurant_id": i,
        "category": category,
        "city": city,
        "commission_rate": categories[category],
        "active_flag": True
    })

df_restaurants = pd.DataFrame(restaurants)


# Clientes

customers = []

for i in range(1, 30001):
    city = np.random.choice(list(cities.keys()))
    first_order = START_DATE - timedelta(days=np.random.randint(30, 300))
    customers.append({
        "customer_id": i,
        "first_order_date": first_order.date(),
        "city": city
    })

df_customers = pd.DataFrame(customers)

# Funções Auxiliares


def random_date(start, end):
    delta = end - start
    return start + timedelta(days=np.random.randint(delta.days))

def generate_order_value():
    return round(np.random.gamma(4, 15), 2)  # ticket médio ~ R$60

# Geração dos Pedidos

orders = []

for i in range(1, N_ORDERS + 1):
    restaurant = df_restaurants.sample(1).iloc[0]
    customer = df_customers.sample(1).iloc[0]

    order_value = generate_order_value()
    delivery_fee = round(np.random.uniform(5, 10), 2)

    subsidy = round(np.random.uniform(0, 10), 2)

    courier_base = np.random.uniform(10, 18)
    delivery_cost = round(
        courier_base * cities[restaurant.city]["courier_index"], 2
    )

    payment_fee = round(order_value * 0.03, 2)

    orders.append({
        "order_id": 9_000_000 + i,
        "order_date": random_date(START_DATE, END_DATE).date(),
        "city": restaurant.city,
        "restaurant_id": restaurant.restaurant_id,
        "customer_id": customer.customer_id,
        "order_value": order_value,
        "delivery_fee": delivery_fee,
        "commission_rate": restaurant.commission_rate,
        "subsidy_value": subsidy,
        "delivery_cost": delivery_cost,
        "payment_fee": payment_fee,
        "order_status": "completed"
    })

df_orders = pd.DataFrame(orders)

# Custos fixos

fixed_costs = pd.DataFrame({
    "month": pd.date_range("2024-01-01", "2024-03-01", freq="MS"),
    "tech_cost": [800_000, 820_000, 850_000],
    "marketing_cost": [1_200_000, 1_250_000, 1_300_000],
    "gna_cost": [400_000, 410_000, 420_000]
})

# Exportação para CSV

df_orders.to_csv("data/orders.csv", index=False)
df_cities.to_csv("data/cities.csv", index=False)
df_restaurants.to_csv("data/restaurants.csv", index=False)
df_customers.to_csv("data/customers.csv", index=False)
fixed_costs.to_csv("data/fixed_costs.csv", index=False)

print("✅ Dataset FP&A Food Delivery gerado com sucesso!")

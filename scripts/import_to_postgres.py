import pandas as pd
from sqlalchemy import create_engine, text

DB_USER = "postgres"
DB_PASSWORD = "123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "food_delivery_fpna"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


DATA_PATH = r"C:/Users/rafap/OneDrive/Documentos/fp&a-food-delivery/data"

files = {
    "customers": "customers.csv",
    "restaurants": "restaurants.csv",
    "cities": "cities.csv",
    "fixed_costs": "fixed_costs.csv",
    "orders": "orders.csv"
}


with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS analytics"))


def load_csv(table_name, file_name):
    df = pd.read_csv(f"{DATA_PATH}/{file_name}")

    df.to_sql(
        table_name,
        engine,
        schema="analytics",
        if_exists="replace",   # replace na 1ª carga
        index=False,
        method="multi",
        chunksize=10_000
    )

    print(f"{table_name} carregada com sucesso ({len(df)} linhas)")

for table, file in files.items():
    load_csv(table, file)


import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DB_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/transactions_db"))

users = pd.read_csv("data/users.csv")
txs = pd.read_csv("data/transactions.csv")

users.to_sql("users", engine, if_exists="append", index=False)
txs.to_sql("transactions", engine, if_exists="append", index=False)
print("✔ Данные загружены в БД")
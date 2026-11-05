import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    # Название БД изменено на transactions_db
    url = os.getenv("DB_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/transactions_db")
    return create_engine(url)

def load_data(engine):
    # Названия таблиц изменены на users и transactions
    users = pd.read_sql("SELECT * FROM users", engine)
    txs = pd.read_sql("SELECT * FROM transactions", engine)
    return users, txs
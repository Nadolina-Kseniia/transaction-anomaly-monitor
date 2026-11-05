import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

np.random.seed(42)
N_USERS = 100
N_TXS = 10000
START = datetime(2026, 1, 1)

# Создаем пользователей
users = pd.DataFrame({
    "user_id": range(1, N_USERS + 1),
    "segment": np.random.choice(["Retail", "VIP", "Business"], N_USERS)
})

# Создаем транзакции
rows = []
for tx_id in range(1, N_TXS + 1):
    user_id = np.random.randint(1, N_USERS + 1)
    date = START + timedelta(days=np.random.randint(0, 30), hours=np.random.randint(0, 23))

    # Обычная транзакция (средний чек ~1000 руб)
    amount = max(10, int(np.random.normal(1000, 300)))

    # Добавляем 2% аномалий (очень крупные суммы)
    if np.random.rand() < 0.02:
        amount = np.random.randint(10000, 50000)

    rows.append({
        "tx_id": tx_id,
        "user_id": user_id,
        "tx_time": date,
        "amount": amount,
        "category": np.random.choice(["Food", "Tech", "Travel", "Bills"])
    })

txs = pd.DataFrame(rows)
Path("data").mkdir(exist_ok=True)
users.to_csv("data/users.csv", index=False)
txs.to_csv("data/transactions.csv", index=False)
print("✔ Данные сгенерированы")
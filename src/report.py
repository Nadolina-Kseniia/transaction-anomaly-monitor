import matplotlib.pyplot as plt
from pathlib import Path


def save_report(df, pivot, daily):
    Path("outputs").mkdir(exist_ok=True)

    # Сохраняем таблицы
    df.to_csv("outputs/scored_transactions.csv", index=False)
    pivot.to_csv("outputs/anomalies_by_segment.csv")

    # График: синие точки — норма, красные — аномалии
    fig, ax = plt.subplots(figsize=(10, 5))

    normal = df[df["is_anomaly"] == 0]
    anomalies = df[df["is_anomaly"] == 1]

    ax.scatter(normal["user_id"], normal["amount"], c="blue", alpha=0.3, label="Normal")
    ax.scatter(anomalies["user_id"], anomalies["amount"], c="red", alpha=0.8, label="Anomaly", marker="X")

    ax.set_title("Транзакции пользователей: поиск аномалий (Z-score > 3)")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Сумма (руб)")
    ax.legend()

    fig.savefig("outputs/anomalies_scatter.png", dpi=120, bbox_inches="tight")
    print("✔ Графики сохранены")
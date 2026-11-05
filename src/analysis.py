import numpy as np
import pandas as pd


def detect_anomalies(txs: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # 1. merge
    df = txs.merge(users, on="user_id", how="left")

    # 2. groupby + transform
    # Считаем средний чек и стандартное отклонение для каждого клиента
    df["user_mean"] = df.groupby("user_id")["amount"].transform("mean")
    df["user_std"] = df.groupby("user_id")["amount"].transform("std")

    # 3. np.where
    # Z-score: насколько транзакция отклоняется от среднего клиента
    # Если Z-score > 3, это аномалия
    df["z_score"] = (df["amount"] - df["user_mean"]) / df["user_std"]

    df["is_anomaly"] = np.where(df["z_score"] > 3.0, 1, 0)

    # 4. str.join (добавим красивый лог)
    def format_log(row):
        if row["is_anomaly"] == 1:
            return "|".join(["ANOMALY", row["segment"], row["category"]])
        return "NORMAL"

    df["tag"] = df.apply(format_log, axis=1)

    return df


def aggregate_stats(df: pd.DataFrame):
    # 5. unstack — сводная таблица: сегменты клиентов на типы категорий
    pivot = df[df["is_anomaly"] == 1].groupby(["segment", "category"]).size().unstack(fill_value=0)

    # 6. cumsum — накопление аномалий по дням
    df["date"] = pd.to_datetime(df["tx_time"]).dt.date
    daily_anomalies = df.groupby("date")["is_anomaly"].sum().reset_index()
    daily_anomalies["cum_anomalies"] = daily_anomalies["is_anomaly"].cumsum()

    return pivot, daily_anomalies
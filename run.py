from src.db import get_engine, load_data
from src.analysis import detect_anomalies, aggregate_stats
from src.report import save_report


def main():
    engine = get_engine()
    users, txs = load_data(engine)

    df = detect_anomalies(txs, users)
    pivot, daily = aggregate_stats(df)

    save_report(df, pivot, daily)
    print(f"✔ Найдено аномалий: {df['is_anomaly'].sum()}")


if __name__ == "__main__":
    main()
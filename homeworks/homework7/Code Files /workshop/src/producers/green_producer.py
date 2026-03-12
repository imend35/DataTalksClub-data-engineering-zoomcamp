
import json
from time import time

import pandas as pd
from kafka import KafkaProducer


TOPIC_NAME = "green-trips"
BOOTSTRAP_SERVERS = ["localhost:9092"]

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-10.parquet"

COLUMNS = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "passenger_count",
    "trip_distance",
    "tip_amount",
    "total_amount",
]


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def row_to_message(row: pd.Series) -> dict:
    msg = row.to_dict()

    # Convert datetime columns to string.
    for col in ["lpep_pickup_datetime", "lpep_dropoff_datetime"]:
        if pd.notna(msg[col]):
            msg[col] = pd.Timestamp(msg[col]).strftime("%Y-%m-%d %H:%M:%S")
        else:
            msg[col] = None

    # Clear NaN values to None for JSON serialization.
    for key, value in msg.items():
        if pd.isna(value):
            msg[key] = None

    return msg


def main():
    df = pd.read_parquet(URL, columns=COLUMNS)

    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=json_serializer
    )

    t0 = time()

    for _, row in df.iterrows():
        message = row_to_message(row)
        producer.send(TOPIC_NAME, value=message)

    producer.flush()

    t1 = time()
    print(f"rows: {len(df)}")
    print(f"took {(t1 - t0):.2f} seconds")


if __name__ == "__main__":
    main()

import json
from kafka import KafkaConsumer

TOPIC = "green-trips"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    consumer_timeout_ms=5000
)

count = 0

for message in consumer:
    trip = message.value
    
    distance = trip.get("trip_distance")
    
    if distance is not None and float(distance) > 5:
        count += 1

consumer.close()

print("Trips with distance > 5 km:", count)
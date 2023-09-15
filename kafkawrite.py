from kafka import KafkaProducer
import json
from json import dumps

p = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)
data = {
    "name": "roscoe",
    "bandwidth": "32mbps",
    "location": {"type": "Point", "coordinates": [40, 5]},
}
p.send("orders", value=data)
p.flush()

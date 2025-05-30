from kafka import KafkaProducer
import json
import time


producer = KafkaProducer(
    bootstrap_servers='195.235.211.197:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open("./parte3_streaming/streaming_sample.json", "r") as f:
    for line in f:
        mensaje = json.loads(line)
        producer.send("energyConsumption", value=mensaje)
        print("Enviado:", mensaje)
        time.sleep(1)  

producer.flush()

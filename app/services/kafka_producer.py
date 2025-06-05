from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

venda = {
    'id_venda': 1,
    'produto': 'Camiseta Branca',
    'quantidade': 2,
    'valor': 59.90,
    'data': '2025-04-19'
}

while True:
    producer.send('vendas', venda)
    print("Venda enviada:", venda)
    time.sleep(5)

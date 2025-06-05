from kafka import KafkaConsumer
import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['frente_caixa']
collection = db['vendas']

consumer = KafkaConsumer(
    'vendas',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

for message in consumer:
    venda = message.value
    collection.insert_one(venda)
    print("Venda salva no MongoDB:", venda)

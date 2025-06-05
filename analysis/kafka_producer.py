from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Exemplo de dados de vendas
venda = {"id": 1, "produto": "Camisa", "quantidade": 2, "preco": 50}

# Envia a mensagem para o tópico 'vendas'
producer.send('vendas', value=venda)

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('vendas', group_id='vendas-group', bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print(f"Nova venda recebida: {message.value}")

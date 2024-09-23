from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'vendas',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest', 
    enable_auto_commit=True,      
    group_id='vendas-group'
)

for message in consumer:
    print(f"Mensagem recebida: {message.value.decode('utf-8')}")
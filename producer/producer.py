from kafka import KafkaProducer
import csv

producer = KafkaProducer(bootstrap_servers='localhost:9092')

with open('vendas.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        producer.send('vendas', value=str(row).encode('utf-8'))

producer.flush()
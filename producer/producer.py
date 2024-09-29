from kafka import KafkaProducer
import csv

# Configurando o produtor Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Abrindo o arquivo vendas.csv para leitura
with open('producer/vendas.csv', 'r') as file:
    reader = csv.reader(file)  # Definindo o leitor CSV
    for row in reader:
        # Enviando a linha como mensagem para o tópico 'vendas'
        producer.send('vendas', value=str(row).encode('utf-8'))
        print(f'Mensagem enviada: {row}')  # Adiciona o print para verificar as mensagens enviadas

# Garantindo que todas as mensagens foram enviadas
producer.flush()

# Fechando o producer
producer.close()
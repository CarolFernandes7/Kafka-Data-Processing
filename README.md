# Kafka-Data-Processing
Projeto Kafka – Pós Graduação Mackenzie

## Estrutura do Projeto

- **producer/producer.py**: Este script lê um arquivo `vendas.csv` e envia as linhas como mensagens para o tópico Kafka chamado `vendas`.
- **consumer/consumer.py**: Este script consome as mensagens do tópico `vendas` e imprime as mensagens no console.

## Requisitos

- **Docker**: Para rodar o Kafka e Zookeeper.
- **Python 3.x**: Para executar os scripts de Producer e Consumer.
- **Bibliotecas**: kafka-python.

## Instruções

1. Execute o comando abaixo para subir os containers Docker:

bash docker-compose up

2. Para rodar o Producer e enviar os dados do arquivo CSV, execute:
   
python3 producer/producer.py

3. Para rodar o Consumer e receber as mensagens do tópico, execute:
   
python3 consumer/consumer.py

4. O arquivo vendas.csv tem o seguinte formato:

produto,quantidade,preco
produto1,10,100
produto2,5,50
produto3,20,200




from dotenv import load_dotenv
import os
import pika
# RabbitMQ credentials
# RabbitMQ credentials
rabbitmq_user = os.environ.get('RABBITMQ_USER')
rabbitmq_password = os.environ.get('RABBITMQ_PASSWORD')
rabbitmq_credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
# Establishing connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='some-rabbit', credentials=rabbitmq_credentials))
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# Establishing connection with RabbitMQ
rabbitmq_host = os.environ.get('RABBITMQ_HOST')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, credentials=rabbitmq_credentials))
channel = connection.channel()
def callback(ch, method, properties, body):
    print("Received message from Microservice B:", body.decode())

# Start consuming messages from RabbitMQ
channel.basic_consume(queue='microservice_b_queue', on_message_callback=callback, auto_ack=True)

print('Microservice A is waiting for messages from Microservice B. To exit press CTRL+C')
channel.start_consuming()

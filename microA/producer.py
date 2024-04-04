import pika
import os
from dotenv import load_dotenv

load_dotenv()

# RabbitMQ credentials
rabbitmq_user = os.environ.get('RABBITMQ_USER')
rabbitmq_password = os.environ.get('RABBITMQ_PASSWORD')
# rabbitmq_credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
rabbitmq_host = os.environ.get('RABBITMQ_HOST')
amqp_url = f'amqps://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_host}'

# Establishing connection with RabbitMQ
# rabbitmq_host = os.environ.get('RABBITMQ_HOST')
print("RabbitMQ Host:", amqp_url)
connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, credentials=rabbitmq_credentials))
channel = connection.channel()


# Declare queues for sending messages from Microservice A to Microservices B and C respectively
channel.queue_declare(queue='microservice_b_queue')
channel.queue_declare(queue='microservice_c_queue')

def send_message_to_b(message):
    channel.basic_publish(exchange='', routing_key='microservice_b_queue', body=message)
    print("Message sent from Microservice A to Microservice B:", message)

def send_message_to_c(message):
    channel.basic_publish(exchange='', routing_key='microservice_c_queue', body=message)
    print("Message sent from Microservice A to Microservice C:", message)

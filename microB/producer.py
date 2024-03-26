
import pika

# Establishing connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue for sending messages from Microservice B to Microservice A
channel.queue_declare(queue='microservice_b_queue')

def publish_to_microservice_a(message):
    channel.basic_publish(exchange='', routing_key='microservice_b_queue', body=message)
    print("Message sent from Microservice B to Microservice A:", message)

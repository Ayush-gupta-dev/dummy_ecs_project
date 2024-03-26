import pika

# RabbitMQ credentials
# rabbitmq_credentials = pika.PlainCredentials('user', 'password')

# Establishing connection with RabbitMQ
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=rabbitmq_credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
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

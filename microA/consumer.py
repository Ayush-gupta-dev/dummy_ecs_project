import pika

# RabbitMQ credentials
rabbitmq_credentials = pika.PlainCredentials('user', 'password')

# Establishing connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=rabbitmq_credentials))
channel = connection.channel()

# Declare a queue for receiving messages from Microservice B
channel.queue_declare(queue='microservice_b_queue')

def callback(ch, method, properties, body):
    print("Received message from Microservice B:", body.decode())

# Start consuming messages from RabbitMQ
channel.basic_consume(queue='microservice_b_queue', on_message_callback=callback, auto_ack=True)

print('Microservice A is waiting for messages from Microservice B. To exit press CTRL+C')
channel.start_consuming()

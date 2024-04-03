import pika

rabbitmq_credentials = pika.PlainCredentials('user', 'password')


# Establishing connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='some-rabbit', credentials=rabbitmq_credentials))
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# Declare a queue for receiving messages from Microservice A
channel.queue_declare(queue='microservice_b_queue')

def callback(ch, method, properties, body):
    print("Received message from Microservice A:", body.decode())

# Start consuming messages from RabbitMQ
channel.basic_consume(queue='microservice_b_queue', on_message_callback=callback, auto_ack=True)

print('Microservice B is waiting for messages from Microservice A. To exit press CTRL+C')
channel.start_consuming()

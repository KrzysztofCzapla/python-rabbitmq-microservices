import pika

from shared.config import QUEUE_NAME


def connect_to_channel_and_queue():
    credentials = pika.PlainCredentials('user', 'password')
    connection_parameters = pika.ConnectionParameters('rabbitmq', credentials=credentials)
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    return channel, connection


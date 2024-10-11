from shared.config import QUEUE_NAME
from shared.rabbitmq_funcs import connect_to_channel_and_queue


def send_message_to_queue(channel, message: str):
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          body=message)


def send(message: str):
    channel, connection = connect_to_channel_and_queue()
    send_message_to_queue(channel, message)
    connection.close()

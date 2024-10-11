from shared.config import QUEUE_NAME
from shared.rabbitmq_funcs import connect_to_channel_and_queue


def get_message(channel):
    method_frame, header_frame, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=False)
    if method_frame:
        channel.basic_ack(method_frame.delivery_tag)
        return body.decode()
    else:
        return None


def receive():
    channel, connection = connect_to_channel_and_queue()
    message = get_message(channel)
    connection.close()
    return message

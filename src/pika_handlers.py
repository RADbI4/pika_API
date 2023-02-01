import os
import pika
from functools import partial


class RabbitMQHandlerFactory:
    """
    Фабрика по созданию обработчиков RabbitMQ
    """

    def __init__(self):
        self.exchange = ''
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def publisher_handler(self, **que_args):
        """
        Publisher сообщений в очереди.
        :return:
        """
        queue = que_args.get('queue')
        routing_key = que_args.get('routing_key')
        self.channel.queue_declare(queue=queue)
        return partial(self.channel.basic_publish, exchange=self.exchange, routing_key=routing_key)

    def consumer_handler(self, **que_args):
        """
        Consumer сообщений очереди.
        :return:
        """
        queue = que_args.get('queue')
        self.channel.queue_declare(queue=queue)
        self.channel.basic_consume(queue=queue, auto_ack=que_args.get('auto_ack'),
                                   on_message_callback=que_args.get('callback_func'))
        return self.channel.start_consuming()


class RabbitMQAmpq_conn:
    """
    Класс для подключения к серверу RabbitMQ.
    """
    username = os.environ.get('')
    pswd = os.environ.get('')
    host = os.environ.get('')
    virt_host = os.environ.get('')


class Queues:
    """
    Класс всех существующих очередей
    """

    """
    Параметры подключения к очереди work_d_out
    """
    work_d_out_params = {
        'queue': 'work_d_out',
        'routing_key': 'work_d_out',
        'auto_ack': True,
    }

    """
    Параметры подключения к очереди work_d_in
    """
    work_d_in_params = {
        'queue': 'work_d_in',
        'routing_key': 'work_d_in',
        'auto_ack': True,
        'callback_func': None
    }

if __name__ == "__main__":
    # telegram_publish = RabbitMQHandlerFactory().publisher_handler(**Queues.work_d_in_params)
    # telegram_publish(body='hello')
    # Queues.work_d_in_params['callback_func'] = callback
    # agent = RabbitMQHandlerFactory().consumer_handler(**Queues.work_d_in_params)
    pass

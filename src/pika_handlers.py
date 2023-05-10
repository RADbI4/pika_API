import pika as p
from contextlib import contextmanager


class RabbitMQHandler:
    """
    Фабрика по созданию обработчиков RabbitMQ очередей
    """

    def __init__(self, host, username=None, password=None):
        self.host = host
        if self.host != 'localhost':
            creds = p.PlainCredentials(username, password)
            conn_params = p.ConnectionParameters(host=self.host, credentials=creds, port=15672)
        else:
            conn_params = p.ConnectionParameters(host)
        self.conn_broker = p.BlockingConnection(conn_params)
        self.channel = self.conn_broker.channel()
        self.channel.basic_qos(prefetch_count=1)  # message consume count
        self.queues = []
        self.priority = None
        self.durable = True

    def queue_bind(self, q_cls):
        self.channel.queue_declare(queue=q_cls.queue, durable=self.durable)
        self.queues.append(q_cls.queue)

    def start_consuming(self, agent_func):
        for queue in self.queues:
            self.channel.basic_consume(on_message_callback=agent_func, queue=queue)
        print(' [*] Waiting for messages, press CTRL+C to exit')
        self.channel.start_consuming()

    def publish_message(self, msg, queue_cls, headers={}):
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_cls.msg_routing_key,
            body=msg,
            properties=p.BasicProperties(
                content_type='application/json',
                delivery_mode=2,
                headers=headers,
                priority=self.priority
            ),
        )

    def broker_close(self):
        self.conn_broker.close()

    @staticmethod
    @contextmanager
    def rabbit_connector(**kwargs):
        """
        Контекстный менеджер по
        подключение к очередям RabbitMQ
        и закрытию коннекта к нему.
        :return:
        """
        agent = RabbitMQHandler(kwargs.get('conn'))
        agent.queue_bind(kwargs.get('queue'))
        try:
            yield agent
        finally:
            agent.broker_close()


# def agent_consumer(callback, conn, **kwargs):
#     agent = RabbitMQHandler(conn)
#     agent.queue_bind(c.WorkDIn)
#     agent.start_consuming(agent_func=callback)
#     agent.broker_close()
#
#
# def agent_publisher(msg, queue, conn):
#     agent_pub = RabbitMQHandler(conn)
#     agent_pub.queue_bind(queue)
#     agent_pub.send_message(msg=msg, queue_cls=queue)
#     agent_pub.broker_close()
#
#
# def callback(ch, method, properties, body):
#     print("Recieved_message")
#     ch.basic_ack(method.delivery_tag)
#     print('Basick_acked')


if __name__ == "__main__":
    # agent_publisher(msg='Hello_world', queue=c.WorkDIn, conn=c.RabbitMQ_conn.local_host)
    # agent_consumer(callback=callback, conn=c.RabbitMQ_conn.local_host)
    pass

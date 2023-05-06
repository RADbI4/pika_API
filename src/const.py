import os


class RabbitMQ_conn:
    """
    Класс для подключения к серверу RabbitMQ.
    """
    params = {'host': '0.0.0.0',
              'username': os.environ.get('rabbit_login'),
              'password': os.environ.get('rabbit_pswd'),
              }
    local_host = 'localhost'


class RabbitMQServers:
    localhost = 'localhost'
    k8s_RabbitMQ_pod = ''


class Queues(object):
    """
    Класс всех существующих очередей
    """
    pass


class WorkDOut(Queues):
    # Параметры подключения к очереди work_d_out
    queue = 'work_d_out'
    routing_key = 'work_d_out'


class WorkDIn(Queues):
    # Параметры подключения к очереди work_d_in
    queue = 'work_d_in'
    msg_routing_key = 'work_d_in'


class GoogeCloudIn(Queues):
    # Параметры подключения к очереди g_cloud_in
    queue = 'g_cloud_in'
    msg_routing_key = 'g_cloud_in'


class YaDiskIn(Queues):
    # Параметры подключения к очереди ya_disk_in
    queue = 'ya_disk_in'
    msg_routing_key = 'ya_disk_in'


class YaDiskOut(Queues):
    # Параметры подключения к очереди ya_disk_in
    queue = 'ya_disk_out'
    msg_routing_key = 'ya_disk_out'


class Exchangers(object):
    """
    Класс для обменников
    """
    pass


class TgFiles(Exchangers):
    exchange_type = 'tg_files'
    exchange = 'fanout'


if __name__ == '__main__':
    pass

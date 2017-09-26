import logging
import sys
from kazoo.client import KazooClient
from kazoo import handlers
class ZKClient:
    def __init__(self, zk_url, zk_timeout=5):
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        self.logger = logging.getLogger()
        try:
            self.client = KazooClient(hosts=zk_url)
            self.client.start(timeout=zk_timeout)
        except handlers.threading.KazooTimeoutError:
            self.logger.error("5 seconds connection timeout")
            raise
    def store_value(self, value, path):
        fmt_value = str(value).encode('utf-8')
        self.client.ensure_path(path)
        self.client.set(path, fmt_value)
        self.client.stop()
    def retrieve_value(self, path):
        self.client.ensure_path(path)
        data, stat = self.client.get(path)
        self.client.stop()
        if not data:
            raise ValueError
        else:
            return int(data.decode('utf-8'))

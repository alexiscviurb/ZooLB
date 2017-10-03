import time

from socket import gethostname

from zookeeper.client import ZKClient

class BkClient:
    def __init__(self, zk_host):
        self.zk = ZKClient(zk_host)

    def get_hostname(self):
        self.hostname = gethostname()
        return self.hostname

    def register_server(self, znode, host, port):
        if not host:
            host = self.get_hostname()
        str_path = '%s/%s:%s' % (znode, host, port)
        self.zk.register_server(str_path)
        while True:
            time.sleep(5)

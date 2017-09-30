import sys

from zookeeper.client import ZKClient

class LbClient:
    def __init__(self):
        ZKClient(args.zk_host)
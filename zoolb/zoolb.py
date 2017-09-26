import argparse
import getpass
import sys

from zookeeper.client import ZKClient

def zk():

def main():
    """
    The "main" entry that controls the flow of the script based
    on the provided arguments.
    """
    # Parse arguments
    parser = argparse.ArgumentParser(
        description = "Módulo Python para gerenciamento automático de Load Balancers Backends.")
    parser.add_argument('--zkhost', action='store', dest='zkhost',
                        required = True,
                        help = 'The address and port of Zookeeper quorum')
    parser.add_argument('--znode', action='store', dest='znode',
                        help = 'The target Znode')
    parser.add_argument('--backend-port', action='store', dest='backend-port',
                        help='The backend Port')
    parser.add_argument('--load-balance', action='store_const', dest='load-balance',
                        const=True, default=False,
                        help='Whether to use load-balance mode')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()



if __name__ == '__main__':
    main()

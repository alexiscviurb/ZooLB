import argparse
import getpass
import sys
import os
from zookeeper.client import ZKClient

# Configuration
DEFAULT_BACKEND_PORT = 8080
DEFAULT_BACKEND_PORT = 8080
DEFAULT_LB_PROVIDER = 'nginx'

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description = "Modulo Python para gerenciamento automatico de Load Balancers Backends.")
    parser.add_argument('--zkhost', action='store', dest='zkhost',
                        default=os.environ.get('ZKHOST', None),
                        help = 'The address and port of Zookeeper quorum')
    parser.add_argument('--znode', action='store', dest='znode',
                        default=os.environ.get('ZNODE', None),
                        help = 'The target Znode')
    parser.add_argument('--mode', choices=['lb', 'backend'], const='backend',
                        default='backend', nargs='?',
                        help='The execution mode. Default to backend')
    parser.add_argument('--version', action='version', version='%(prog)s 0.2.0')

    arg_group_backend = parser.add_argument_group('Backend')
    arg_group_backend.add_argument('--backend-port', action='store', dest='backend_port',
                                   default=DEFAULT_BACKEND_PORT, metavar='PORT',
                                   help='The port of backend listen. Defaults to {0} '.format(DEFAULT_BACKEND_PORT))  
    arg_group_backend.add_argument('--backend-host', action='store', dest='backend_host',
                                   default=DEFAULT_BACKEND_HOST, metavar='HOST',
                                   help='The address/hostname of backend. Defaults to {0} '.format(DEFAULT_BACKEND_HOST))  

    arg_group_lb = parser.add_argument_group('Load Balance')
    arg_group_lb.add_argument('--lb-provider', action='store', dest='lb_provider',
                              default=DEFAULT_LB_PROVIDER, metavar='PROVIDER',
                              help='The provider of load balance. Defaults to {0} '.format(DEFAULT_LB_PROVIDER))  

    args = parser.parse_args()

    if not args.zkhost:
        exit(parser.error("the following arguments are required: --zkhost"))

    if not args.znode:
        exit(parser.error("the following arguments are required: --znode"))

    print (args)

if __name__ == '__main__':
    main()

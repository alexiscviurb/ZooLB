import argparse
import getpass
import sys

def zk():

def main():
    """
    The "main" entry that controls the flow of the script based
    on the provided arguments.
    """
    # Parse arguments
    parser = argparse.ArgumentParser(
        description = "Módulo Python para gerenciamento automático de Load Balancers Backends.")
    parser.add_argument('-H', '--hostname', action='store', dest='hostname',
                        required = True,
                        help = 'The hostname of the Cloudera Manager server.')
    parser.add_argument('-p', action='store', dest='port', type=int,
                        help = 'The port of the Cloudera Manager server. Defaults '
                        'to 7180 (http) or 7183 (https).')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()



if __name__ == '__main__':
    main()

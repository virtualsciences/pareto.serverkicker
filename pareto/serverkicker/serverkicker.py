import os
import sys
import urllib2
import socket
import argparse

def command():
    description = """\
    This script checks for the availability of a web service, and if said
    service is not available, calls a command to (re)boot it.
    """

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        'checkurl', metavar='URL', type=str, nargs=1,
        help='URL to check')
    parser.add_argument(
        '-t', dest='timeout', action='store', type=float, default=30,
        help='Timeout (in seconds, default 30)')
    parser.add_argument(
        '-c', dest='command', action='store', type=str, default=None,
        help='Command to execute if the server is not available (default None)')

    args = parser.parse_args()
    url = args.checkurl[0]
    try:
        urllib2.urlopen(url, timeout=args.timeout)
    except (urllib2.URLError, socket.error):
        if args.command:
            os.system(args.command)
        # exit with error code
        sys.exit(1)

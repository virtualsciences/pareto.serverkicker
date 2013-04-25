import os
import sys
import urllib2
import socket
import optparse

def command():
    description = """
    %s [-t <timeout>] [-c <command>] url

    This script checks for the availability of a web service, and if said
    service is not available, calls a command to (re)boot it.
    """ % (sys.argv[0],)

    parser = optparse.OptionParser(usage=description)
    parser.add_option(
        '-t', dest='timeout', action='store', type=float, default=30,
        help='Timeout (in seconds, default 30)')
    parser.add_option(
        '-c', dest='command', action='store', type=str, default=None,
        help=(
            'Command to execute if the server is not available'
            ' (default None)'))

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error('expecting a single URL as argument')
    url = args[0]
    if timeout:
        # we can't pass timeout as arg for urlopen() if we want to support
        # python <= 2.4
        socket.setdefaulttimeout(options.timeout)
    try:
        urllib2.urlopen(url)
    except (urllib2.URLError, socket.error):
        if options.command:
            os.system(options.command)
        # exit with error code
        sys.exit(1)

if __name__ == '__main__':
    command()

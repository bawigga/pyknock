#!/usr/bin/env python

import argparse
import socket
import logging
import inspect
import pprint
from Scanner import Scanner

OPTS=None

def process_args():
    parser = argparse.ArgumentParser(description="Simple python port scanner")

    # version information
    parser.add_argument('--version', action='version', version="%(prog)s 0.1 - Brian Wigginton <brianwigginton@gmail.com>")
    
    # get the target ip address
    parser.add_argument('ip', help="target ip address");
    
    # get the port number to scan
    parser.add_argument('-p', '--port', help="target port to scan", type=int);

    # get the number of threads to run
    parser.add_argument('-t', '--num_threads', help="number of threads to use", default=3, type=int);

    # get verbosity
    parser.add_argument('-v', '--verbose', help="set verbosity", action='store_true')

    # get debug level
    parser.add_argument('-d', '--debug', help="debug", action='store_true');

    global OPTS
    OPTS = parser.parse_args()

    if(OPTS.debug): logging.basicConfig(level=logging.DEBUG)

    # handle default port numbers
    if(OPTS.port == None):
        OPTS.port = range(1, 1025)


def main():
    process_args()
    
    print "Scanning {0}...\n".format(OPTS.ip)

    Scanner(OPTS.ip, OPTS.port, num_threads=OPTS.num_threads)
    
    print "\nDone."

if(__name__ == "__main__"):
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Vítor Brandão <vitor@noiselabs.io>

import argparse
import os
import socket
import subprocess
import sys

def is_ghost_running(address, port):
    """
    Check if the Ghost service is up and running.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    is_running = s.connect_ex((address, port)) == 0
    s.close()
    return is_running


def fix_urls(local_address, local_port, live_url, static_dir):
    if os.path.isfile(os.path.join(static_dir, 'rss/index.html')):
        os.rename(os.path.join(static_dir, 'rss/index.html'),
                  os.path.join(static_dir, 'rss/index.rss'))

    for root, dirs, files in os.walk(static_dir):
        for file in files:
            if file.endswith('.html') or file.endswith('.rss'):
                with open(os.path.join(root, file), 'rU+') as f:
                    content = f.read()
                    f.seek(0)
                    f.truncate()
                    content = content.replace(
                        'http://%s:%s' % (local_address, local_port), live_url)
                    content = content.replace(
                        'rss/index.html', 'rss/index.rss')
                    f.write(content)

def generate():
    """
    Blah.
    """
    try:
        address = str(os.getenv('GHOST_LOCAL_ADDRESS'))
    except TypeError:
        raise Exception("Environment variable `GHOST_LOCAL_ADDRESS` is not defined")
    try:
        port = int(os.getenv('GHOST_LOCAL_PORT'))
    except TypeError:
        raise Exception("Environment variable `GHOST_LOCAL_PORT` is not defined")
    if not is_ghost_running(address, port):
        raise Exception("Ghost isn't running at %s:%d\nPlease start it with `docker-compose up web -d`" % (address, port))

    static_dir = os.getenv('BUSTER_STATIC_DIR')
    subprocess.call(['buster', 'generate', '--domain=%s:%d' % (address, port), '--dir=%s' % static_dir], stdout=sys.stdout, stderr=sys.stderr)
    live_url = os.getenv('LIVE_URL')
    fix_urls(address, port, live_url, static_dir)

def preview():
    pass

def deploy():
    pass    

def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description='Wrapper for Buster.')
    parser.add_argument('action', action='store', type=str, help='Buster action')

    args = parser.parse_args()

    if args.action == 'generate':
        generate()
    else:
        raise ValueError('Unrecognized action "%s"' % args.action)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.stdout.write('\033[91m[ERROR]\033[0m %s' % str(e))
        sys.exit(-1)

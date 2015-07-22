#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from rest_client import RestClient

if __name__ == '__main__':
    # parse parameters
    parser = argparse.ArgumentParser(
        description="Send API calls to easy_phi web application. "
                    "Results will be printed to console")
    parser.add_argument('--host', default='http://localhost:8000',
                        help='Easy Phi platform network name')
    parser.add_argument('-s', '--slot', default=0, help='slot number, 0..31')
    parser.add_argument('-a', '--api-token', default='',
                        help='API token, login and look at the top left corner '
                             'of web interface')
    parser.add_argument('cmd', help='SCPI command to send')
    args = parser.parse_args()

    rc = RestClient(args.host, args.api_token or None)

    print rc.scpi(args.slot, args.cmd)


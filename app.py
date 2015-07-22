#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import settings
from rest_client import RestClient

# parse parameters
parser = argparse.ArgumentParser(
    description="Send API calls to easy_phi web application. "
                "Results will be printed to console")
parser.add_argument('-s', '--slot', default=0, help='slot number, int')
parser.add_argument('-scpi', '--scpi_command', default='*IDN?', help='scpi command, char')
args = parser.parse_args()

slot = args.slot
scpi = args.scpi_command
rc = RestClient(settings.base_url)

# platform info
pi = rc.get_platform_info()
print 'Platform info: ' + pi

# module info
mi = rc.get_module_info(slot)
print 'Information about module in slot {}: '.format(slot) + mi

# modules list
ml = rc.get_modules_list()
print 'Modules list: ' + ml

# module scpi list
scpl = rc.get_module_scpi_list(slot)
print 'SCPI list for module in slot {}: '.format(slot) + scpl

# module lock/unlock
mlck = rc.lock_module(slot)
print 'Module lock/unlock status: ' + mlck

# send scpi
scpi = rc.send_scpi(slot, scpi)
print 'SCPI command sent to module in slot {}. Response is '.format(slot) + scpi

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
#import easy_phi_client

import settings
from easy_phi_client import PythonClient



# parse parameters
parser = argparse.ArgumentParser(
description="Send API calls to easy_phi web application. "
			"Results will be printed to console")
parser.add_argument('-s', '--slot', help='slot number, int')
args = parser.parse_args()

if args.slot is None:
	slot = 0
else:
	slot = args.slot

pc = PythonClient(settings.api_token)

# platform info
pi = pc.get_platform_info()
print 'Platform info: ' + pi
  # logging.debug "Raw platform info JSON:\n %s", json.dumps(pi)

# module info
mi = pc.get_module_info(slot)
print 'Information about nmodule in slot {}: '.format(slot) + mi

# modules list
ml = pc.get_modules_list()
print('Modules list: ' + ml)

# module scpi list
scpl = pc.get_module_scpi_list(slot)
print 'SCPI list for module in slot {}: '.format(slot) + scpl

# module locked?
# mlck = pc.lock_module()
# print('Status of the module: ' + mlck)

# send scpi
scpi = pc.send_scpi(slot)
print 'Status of the module: ' + scpi

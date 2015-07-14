#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import settings
import json
import urllib
import logging
import datetime

class PythonClient(object):

    baseURL = settings.base_url

    def __init__(self, api_token):
        self.logger = logging.getLogger(__name__)
        self.api_token = api_token
        # HTTP Auth magic
        # TODO: replace with urllib2 opener
        chunks = self.baseURL.split("//", 1)
        if len(chunks) < 2:  # no https? in url
            chunks[:0] = 'https:',
        self.baseURL = ''.join((chunks[0], "//",
                                ":".join((self.api_token, 'api_token@')),
                                chunks[1]))

    def _build_url(self, api_func, params):
        # build ULR of API request, which looks like:
        # https://${base_url}/{api_func}?param1=foo&param2=bar
        query = '' if params is None else '?' + urllib.urlencode(params)
        url = ''.join((self.baseURL, api_func, query))
        self.logger.debug("_build_url: %s:" % url)
        return url

    def _get_json(self, url):
        try:
            response = urllib.urlopen(url)
        except IOError:
            self.logger.error('Failed to open url: %s' % url)
            raise
        response = response.read()
        self.logger.debug("Response from: %s" % response)
        return response

    def _request(self, api_func, params=None):
        url = self._build_url(api_func, params)
        return self._get_json(url)


    def get_platform_info(self):
        data = self._request('/api/v1/info')
        return data

    def get_module_info(self, slot):
        data = self._request('/api/v1/module?slot=%s' % slot)
        return data

    def get_modules_list(self):
        data = self._request('/api/v1/modules_list')
        return data

    def get_module_scpi_list(self, slot):
        data = self._request('/api/v1/module_scpi_list?slot=%s' % slot)
        return data

    def lock_module(self):
        data = self._request('/api/v1/lock_moduleslot=%s' % slot)
        return data

    def send_scpi(self):
        data = self._request('/api/v1/send_scpi=%s' % slot, '*IDN?')
        return data


if __name__ == '__main__':

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
    print('Platform info: ' + pi)
    logging.debug("Raw platform info JSON:\n %s", json.dumps(pi))

    # module info
    mi = pc.get_module_info(slot)
    print('Information about nmodule in slot %s: ' % slot + mi)

    # modules list
    ml = pc.get_modules_list()
    print('Modules list: ' + ml)

    # module scpi list
    scpl = pc.get_module_scpi_list(slot)
    print('SCPI list for module in slot %s: ' % slot + scpl)

    # module locked?
    # mlck = pc.lock_module()
    # print('Status of the module: ' + mlck)

    # send scpi
    #   scpi = pc.send_scpi()
    #  print('Status of the module: ' + scpi.read())

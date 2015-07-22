#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import logging


class RestClient(object):
    """THis class is a proxy for Easy Phi system REST API"""

    def __init__(self, base_url):
        self.logger = logging.getLogger(__name__)
        self.baseURL = base_url

    def _request(self, api_func, data=None):
        url = self.baseURL + api_func

        if data:
            body = urllib.urlencode({'': data})
            req = urllib2.Request(url, body)
        else:
            req = urllib2.Request(url)

        try:
            response = urllib2.urlopen(req)
        except IOError:
            self.logger.error('Failed to open url: ' + url)
            raise
        response = response.read()
        self.logger.debug("Response from: " + response)

        return response

    def get_platform_info(self):
        data = self._request('/api/v1/info')
        return data

    def get_module_info(self, slot):
        data = self._request('/api/v1/module?slot=' + str(slot))
        return data

    def get_modules_list(self):
        data = self._request('/api/v1/modules_list')
        return data

    def get_module_scpi_list(self, slot):
        data = self._request('/api/v1/module_scpi_list?slot=' + str(slot))
        return data

    def lock_module(self, slot):
        if slot != 0:
            data = self._request('/api/v1/lock_module?slot=' + str(slot))
        else:
            data = 'Not a valid operation for Broadcast Module'
        return data

    def send_scpi(self, slot, scpi):
        data = self._request('/api/v1/send_scpi?slot=' + str(slot), scpi)
        return data

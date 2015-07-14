#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
import logging

import settings


class PythonClient(object):
    baseURL = settings.base_url

    def __init__(self, api_token):
        self.logger = logging.getLogger(__name__)
        self.api_token = api_token

    def _request(self, api_func, params=None):

        # build ULR of API request, which looks like:
        # https://${base_url}/{api_func}?param1=foo&param2=bar
        query = '' if params is None else '?' + urllib.urlencode(params)
        url = ''.join((self.baseURL, api_func, query))
        self.logger.debug("_build_url: {}:".format(url))

        try:
            response = urllib.urlopen(url)
        except IOError:
            self.logger.error('Failed to open url: {}'.format(url))
            raise
        response = response.read()
        self.logger.debug("Response from: {}".format(response))

        return response

    def get_platform_info(self):
        data = self._request('/api/v1/info')
        return data

    def get_module_info(self, slot):
        data = self._request('/api/v1/module?slot={}'.format(slot))
        return data

    def get_modules_list(self):
        data = self._request('/api/v1/modules_list')
        return data

    def get_module_scpi_list(self, slot):
        data = self._request('/api/v1/module_scpi_list?slot={}'.format(slot))
        return data

    def lock_module(self, slot):
        data = self._request('/api/v1/lock_module?slot={}'.format(slot))
        return data

    def send_scpi(self, slot, scpi):
        params = urllib.urlencode({'body': scpi})
        data = urllib.urlopen('http://localhost:8000/api/v1/send_scpi?slot={}'.format(slot), params)
        return data

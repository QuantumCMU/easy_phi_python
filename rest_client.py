#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import urllib
import json


class RestClient(object):
    """ Wrapper for Easy Phi platform REST API """

    logger = logging.getLogger('easy_phi client')
    base_url = None
    api_token = None

    def __init__(self, base_url='http://localhost:8000', api_token=None):
        self.baseURL = base_url
        self.api_token = api_token

    def _request(self, url, params={}, data=None):
        if 'format' not in params:
            params['format'] = 'json'
        query = '?' + urllib.urlencode(params)
        full_url = ''.join((self.baseURL, url, query))

        self.logger.debug("Request url: %s", full_url)

        if self.api_token is not None:
            # There are three ways to pass api token:
            # 1. set cookie 'api_token' - more secure, but requires building
            #       URL opener, just lazy to make it this time
            # 2. HTTP Basic auth 'api_token:<token_value>' - not secure, but can
            #       be done in couple lines of code
            # 3. GET param - even less secure, but easiest
            full_url += '&api_token=' + self.api_token

        response = urllib.urlopen(full_url, data)
        response_text = response.read()

        self.logger.debug("Response text: %s", response_text)

        if params['format'] == 'json':
            return json.loads(response_text)
        return response_text

    def get_platform_info(self):
        return self._request('/api/v1/info')

    def get_module_info(self, slot):
        return self._request('/api/v1/module', {'slot': slot})

    def get_module_names(self):
        return self._request('/api/v1/modules_list')

    def get_supported_commands(self, slot):
        return self._request('/api/v1/module_scpi_list', {'slot': slot})

    def lock_module(self, slot):
        if not self.api_token:
            raise ValueError("System without api token don't use locks")

        if not 0 < slot < 32:
            raise ValueError("Slot has to be integer in range 1..31")

        return self._request('/api/v1/lock_module', {'slot': slot})

    def unlock_module(self, slot):
        raise NotImplementedError("Unfortunately, urllib is not ver convenient "
                                  "for making DELETE requests, but we hope you "
                                  "already get the idea how to use API.")

    def scpi(self, slot, scpi):
        return self._request('/api/v1/send_scpi', {'slot':slot}, scpi)

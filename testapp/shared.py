import os
import json

from urllib.parse import urlencode

from django.test import TestCase
from django.conf import settings
from django.urls import reverse as rev

from rest_framework.authtoken.models import Token


def reverse(url, params=None, **kwargs):
    """
    :param url:
    :param params: dict
    :return: full_url: full_url
    """
    return rev(url, **kwargs) + '?' + urlencode(params or {})


class ViewSetTestCase(object):
    def _list(self, filters=None, kwargs=None):
        filters = filters or {}
        kwargs = kwargs or {}

        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'list')

        url = reverse(self.url % method, filters, kwargs=kwargs)
        response = self.client.get(url, **headers)
        return response

    def _retrieve(self, kwargs):
        kwargs = kwargs or {}

        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'detail')

        url = reverse(self.url % method, kwargs=kwargs)
        response = self.client.get(url, **headers)
        return response

    def _create(self, data=None, kwargs=None, params=None):
        params = params or {}
        kwargs = kwargs or {}
        data = data or {}

        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'list')

        url = reverse(self.url % method, params=params, kwargs=kwargs)
        response = self.client.post(url, data, **headers)

        return response

    def _bulk_update(self, kwargs, data=None):
        data = data or []
        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'list')

        url = reverse(self.url % method, kwargs=kwargs)
        response = self.client.put(url, data, **headers)
        return response

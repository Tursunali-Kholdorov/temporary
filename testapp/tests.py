from django.test import TestCase

from unittest.mock import patch, Mock, call

from django.db import IntegrityError
from django.utils.translation import gettext
from django.core.cache import cache
from .shared import reverse

from rest_framework.test import APITransactionTestCase, APITestCase
from rest_framework import status

from requests.exceptions import ReadTimeout

from .models import Car
from .shared import ViewSetTestCase
import json


class CarTest(APITransactionTestCase, ViewSetTestCase):
    fixtures = [
        'cars.yaml',
    ]

    url = 'testapp:cars-%s'

    def test_retrieve(self):
        response = self._retrieve({'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "id": 1,
            "name": "mersedes",
            "number": "777",
        })

    def test_list(self):
        response = self._list(filters={'ordering': '-id'}, kwargs={'headers': {'content_type':"application/json"}})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0], {
            "id": 4,
            "name": "audi",
            "number": "111"
        })


class TestUpdate(APITestCase):
    fixtures = [
        'cars.yaml',
    ]

    def test_bulk_update(self):
        url = reverse('testapp:cars-update')
        data = [{'id': 1,
                 'order': 2},
                {'id': 2,
                 'order': 1,
                 }]
        response = self.client.put(
            url,
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

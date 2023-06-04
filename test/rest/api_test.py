import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # Test api add endpoint
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_add_error(self):
        url = f"{BASE_URL}/calc/add/2/A"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400)

    # Test api substract endpoint
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_substract_error(self):
        url = f"{BASE_URL}/calc/substract/a/1"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400)

    # Test api multiply endpoint
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_multiply_error(self):
        url = f"{BASE_URL}/calc/multiply/5/"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 404)

    # Test api divide endpoint
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/25/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_divide_error(self):
        url = f"{BASE_URL}/calc/divide/5/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400)

    # Test api power endpoint
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_power_error(self):
        url = f"{BASE_URL}/calc/power/5/A"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400)

    # Test api sqrt endpoint
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_sqrt_error(self):
        url = f"{BASE_URL}/calc/sqrt/-1"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400)

    # Test api log10 endpoint
    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_log10_error(self):
        url = f"{BASE_URL}/calc/log10/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400)

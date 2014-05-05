from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.login.tests import create_user


class UrlTest(TestCase):

    def test_cookies(self):
        response = self.client.get('/cookies/')
        self.assertEqual(response.status_code, 200)

    def test_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)



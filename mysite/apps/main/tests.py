from django.test import TestCase
from django.contrib.auth.models import User


def create_user(username='test_user'):
    return User.objects.create_user(username=username)


class MainTest(TestCase):
    def setUp(self):
        self.user = create_user()


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

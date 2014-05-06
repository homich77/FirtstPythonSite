from django.test import TestCase
from django.contrib.auth.models import User


def create_user(username='test_user', password=None):
    return User.objects.create_user(username=username, password=password)


class MainTest(TestCase):
    def setUp(self):
        self.user = create_user(password='qwe')


class LoadsTest(TestCase):
    def test_cookies(self):
        response = self.client.get('/cookies/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookies/index.html')

    def test_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/main.html')

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

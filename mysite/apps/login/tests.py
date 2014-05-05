from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def create_user(username='test_user', password='test'):
    return User.objects.create_user(username=username,
                                    password=password)


class LoginClass(TestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_user(self):
        user_from_database = User.objects.get(username=self.user.username)
        self.assertEqual(user_from_database.username, self.user.username)

    def test_login_profile_view(self):
        response = self.client.get(reverse('login:profile',
                                           args=(self.user.username,)))
        self.assertContains(response, self.user.email, status_code=200)

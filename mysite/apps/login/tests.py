from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def create_user():
    user = User(username='test_user')
    user.set_password('test')
    user.save()
    return user


class LoginClass(TestCase):

    def test_create_user(self):
        user = create_user()
        user_from_database = User.objects.get(username=user.username)
        self.assertEqual(user_from_database.username, user.username)

    def test_login_profile_view(self):
        user = create_user()
        response = self.client.get(reverse('login:profile',
                                           args=(user.username,)))
        self.assertContains(response, user.email, status_code=200)
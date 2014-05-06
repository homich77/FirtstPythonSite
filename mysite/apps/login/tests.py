from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from apps.main.tests import MainTest


class LoginTest(MainTest):
    def test_create_user(self):
        user_from_database = User.objects.get(username=self.user.username)
        self.assertEqual(user_from_database.username, self.user.username)

    def test_login_profile(self):
        response = self.client.get(reverse('login:profile',
                                           args=(self.user.username,)))
        self.assertContains(response, self.user.email, status_code=200)

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from apps.main.tests import MainTest


class LoginTest(MainTest):
    def test_create(self):
        user_from_database = User.objects.get(username=self.user.username)
        self.assertEqual(user_from_database.username, self.user.username)

    def test_profile(self):
        response = self.client.get(reverse('login:profile',
                                           args=(self.user.username,)))
        self.assertContains(response, self.user.email, status_code=200)
'''
    def test_user_login(self):
        url_login = reverse('login:user_login')
        response = self.client.post(url_login,
                                    {   'username': self.user.username,
                                        'password': 'qwe' })
        self.assertRedirects(response, url_login, status_code=200)
'''
from django.test import TestCase
from django.contrib.auth.models import User

from apps.cookies.models import Cookie


def create_cookie():
    return Cookie.objects.create(name='test_cookie',
                                 description='description test cookie')

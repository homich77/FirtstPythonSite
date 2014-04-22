from django.db import models
from django.contrib.auth.models import User, UserManager

class UserDetail(User):
    user = models.OneToOneField(User)
    ava = models.ImageField(upload_to= '.')

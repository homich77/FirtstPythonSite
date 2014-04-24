from django.db import models
from django.contrib.auth.models import User

#User.add_to_class('ava', models.ImageField(upload_to='.'))
class UserDetail(models.Model):
    user = models.OneToOneField(User, related_name='user_detail', unique=True)
    ava = models.ImageField(upload_to='.', blank=True)
    about = models.TextField(blank=True)

    def __unicode__(self):
        return  self.user.username

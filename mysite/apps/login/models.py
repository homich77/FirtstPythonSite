from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

'''
class UserDetail(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='user_detail',
                                unique=True)
    ava = models.ImageField(upload_to='.')
    about = models.TextField()

    def __unicode__(self):
        return self.user.username'''


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ava = models.ImageField(upload_to='ava/', blank=True)
    about = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

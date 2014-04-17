from django.db import models
from mysite import settings

class Cookie(models.Model):
    name = models.CharField(max_length=64)
    img = models.ImageField(upload_to=settings.MEDIA_ROOT)
    description = models.CharField(max_length=2048)

    def __unicode__(self):
        return self.name

'''class User(models.Model):
    login = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    ava = models.ImageField()
    about_yourself = models.CharField()

class Recall(models.Model):
    pass'''
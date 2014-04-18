from django.db import models
from templatetags.media import media

class Cookie(models.Model):
    name = models.CharField(max_length=64)
    img = models.ImageField(upload_to='.')
    description = models.CharField(max_length=2048)

    def __unicode__(self):
        return self.name

    def admin_image(self):
        return '<img style="height:100px" src="%s"/>' % media(self.img)
    admin_image.allow_tags = True
    admin_image.short_description = 'Image'

'''class User(models.Model):
    login = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    ava = models.ImageField()
    about_yourself = models.CharField()

class Recall(models.Model):
    pass'''
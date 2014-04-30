from django.conf import settings
from django.db import models
from templatetags.media import media

from .managers import CookieManager, ReviewManager


class Cookie(models.Model):
    name = models.CharField(max_length=64)
    img = models.ImageField(upload_to='.')
    description = models.CharField(max_length=2048)

    objects = CookieManager()

    def __unicode__(self):
        return self.name

    def admin_image(self):
        return '<img style="height:100px" src="%s"/>' % media(self.img)

    admin_image.allow_tags = True
    admin_image.short_description = 'Image'


class Review(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    cookie_id = models.ForeignKey(Cookie)
    text = models.TextField()
    mark = models.IntegerField()
    date = models.DateTimeField()

    objects = ReviewManager()

    def __unicode__(self):
        return self.text

    class Meta:
        #ordering = ['date']
        unique_together = (("user_id", "cookie_id"),)

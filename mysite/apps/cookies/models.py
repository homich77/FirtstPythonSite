from django.db import models
from templatetags.media import media
from django.contrib.auth.models import User

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

class Review(models.Model):
    user_id = models.ForeignKey(User, related_name='user')
    cookie_id = models.ForeignKey(Cookie)
    text = models.TextField()
    mark = models.IntegerField(max_length=5)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.text

    class Meta:
        #ordering = ['date']
        unique_together = (("user_id", "cookie_id"),)

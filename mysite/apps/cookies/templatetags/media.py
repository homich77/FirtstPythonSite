from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def media(filename):
    return settings.MEDIA_URL + str(filename)
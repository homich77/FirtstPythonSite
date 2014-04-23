from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def media(filename):
    return settings.MEDIA_URL + str(filename)

@register.filter
def get_range( value ):
  return range( 1, value + 1)

@register.filter
def get_reverse_range( value ):
  return range( value, 0, -1)
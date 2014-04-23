from django import forms
from django.contrib import admin
from .models import Cookie

class CookieForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))

class CookieAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'description', 'admin_image', )
    form = CookieForm

admin.site.register(Cookie, CookieAdmin)

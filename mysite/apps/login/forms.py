from django import forms
from django.utils.translation import ugettext as _

class UserLoginForm(forms.Form):
    username = forms.CharField(label=_(u'inputUserName'), max_length=30)
    password = forms.CharField(label=_(u'inputPassword'), widget=forms.PasswordInput)
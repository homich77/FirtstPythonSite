from django import forms

from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from apps.login.models import UserDetail

#from django.forms.widgets import PasswordInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UserDetailForm(UserForm):
    class Meta(UserForm.Meta):
        model = UserDetail
        fields = ['ava', 'about']
        widgets = {
            'about': Textarea(attrs={'rows': 4})
        }
        labels = {
            'ava': 'Profile picture'
        }

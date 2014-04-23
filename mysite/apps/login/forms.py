from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm

class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

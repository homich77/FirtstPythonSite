from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from collections import OrderedDict

from multiform import MultiModelForm

from apps.login.models import UserProfile


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['ava', 'about']
        labels = {
            'ava': 'Profile picture',
            'about': 'About yourself'
        }
        widgets = {
            'about': Textarea(attrs={'rows': 4})
        }


class UserMultiForm(MultiModelForm):
    base_forms = OrderedDict([
        ('user', UserForm),
        ('profile', UserProfileForm)
    ])

    def dispatch_init_instance(self, name, instance):
        if name == 'profile':
            return super(UserMultiForm, self).dispatch_init_instance(name,
                                                                     instance)
        else:
            return instance

    def save(self, commit=True):
        instances = super(UserMultiForm, self).save(commit=False)
        instances['profile'].user = instances['user']
        if commit:
            for instance in instances.values():
                instance.save()
        return instances

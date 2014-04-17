from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect


''''
from django.contrib import auth
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template

def user_login_view(request):
    form = UserLoginForm(request.POST or None)
    context = { 'form': form, }
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return redirect('index_page')
    return direct_to_template(request, 'form.html', context)'''
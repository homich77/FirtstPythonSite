from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import auth

def user_login(request):
    error_message = ''
    if request.method == 'POST': #and form.is_valid():
        try:
            username = request.POST['inputUserName']
            password = request.POST['inputPassword']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('cookies:search'))
        except:
            error_message = 'Enter correct data'
    return render_to_response('login/login.html', {'error_message': error_message}, RequestContext(request))

def edit(request):
    pass
from django.forms.models import modelformset_factory
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
                return HttpResponseRedirect(reverse('main:main_view'))
        except:
            error_message = 'The username and password were incorrect.'
    return render_to_response('login/login.html', {'error_message': error_message}, RequestContext(request))

#@login_required
def edit(request):
    if request.method == 'GET':
        return render(request, "login/edit.html")
    else:
        try:
            user = request.user
            user.first_name = request.POST["inputFirstName"]
            user.last_name = request.POST["inputLastName"]
            user.email = request.POST["inputEmail"]
            user.save()
            return render_to_response('login/edit.html', {'success_message': 'Data has been successfully saved'}, RequestContext(request))
        except:
            error_message = "Have error"
        return render_to_response('login/edit.html', {'error_message': error_message}, RequestContext(request))

def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main_view'))
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from apps.login.models import UserDetail


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


def profile(request, user_name):
    user_obj = get_object_or_404(User, username = user_name)
    return render_to_response('login/profile.html', {'user_data': user_obj}, RequestContext(request))


#@login_required
def edit_view(request):
    user_obj = request.user
    #user_detail = UserDetail.objects.get_or_create(user=user_obj,about='')
    return render_to_response("login/edit.html", {}, RequestContext(request))


def edit_save(request):
    try:
        user_obj = request.user
        user_obj.first_name = request.POST["inputFirstName"]
        user_obj.last_name = request.POST["inputLastName"]
        user_obj.email = request.POST["inputEmail"]

        user_detail, created = UserDetail.objects.get_or_create(user=user_obj)
        user_detail.about = request.POST["inputAbout"]

        user_detail.save()
        user_obj.save()

        return HttpResponseRedirect(reverse('login:edit'), {'success_message': 'Data has been successfully saved'})
    except:
        error_message = "Have error"
    return HttpResponseRedirect(reverse("login:edit"), {'error_message': error_message})


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main_view'))
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
#from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from apps.login.models import UserDetail
from apps.cookies.models import Cookie, Review
from apps.login.forms import UserForm, UserDetailForm

from django.core.urlresolvers import resolve
from get_referer import get_referer_view

def user_login(request):
    template = 'login/login.html'

    error_message = ''
    if request.method == "GET":
        error_message = ''
    else:
        try:
            username = request.POST['inputUserName']
            password = request.POST['inputPassword']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return redirect(get_referer_view(request))
        except:
            error_message = 'The username and password were incorrect.'
    return render_to_response(template, {'error_message': error_message}, context_instance = RequestContext(request))

def create(request):
    template = 'login/create.html'
    error_message = ''
    form = UserCreationForm()
    if request.method == "POST":
        try:
            form = UserCreationForm(request.POST)
            form.save()
            return redirect(reverse("login:user_login"), RequestContext(request))
        except:
            error_message = 'You have mistake'
    return render_to_response(template, {'form': form, 'error_message': error_message}, RequestContext(request))


def profile(request, user_name):
    user_obj = get_object_or_404(User, username = user_name)

    best_cookies = Cookie.objects.filter(review__user_id=user_obj)\
                       .filter(review__mark__gte=4)\
                       .order_by("-review__mark")[:10]
    latest_reviews = Review.objects.filter(user_id=user_obj).order_by("-date")[:10]
    context = {'user_data': user_obj,
               'best_cookies': best_cookies,
               'latest_reviews': latest_reviews
    }
    return render_to_response('login/profile.html', context, RequestContext(request))


#@login_required
def edit_view(request):
    user_form = UserForm(instance=request.user)
    detail = UserDetail.objects.get(user=request.user)
    detail_form = UserDetailForm(instance=detail)
    return render_to_response("login/edit.html", {'user_form': user_form, 'detail_form': detail_form}, RequestContext(request))


def edit_save(request):
    user_form = UserForm(request.POST, instance=request.user)
    detail, created = UserDetail.objects.get_or_create(user_id=request.user)
    detail_form = UserDetailForm(request.POST, request.FILES, instance=detail)
    if user_form.is_valid():
        detail_form.save()
        user_form.save()
    return HttpResponseRedirect(reverse("login:edit"), RequestContext(request))
    '''try:
        user_obj = request.user
        user_obj.first_name = request.POST["inputFirstName"]
        user_obj.last_name = request.POST["inputLastName"]
        user_obj.email = request.POST["inputEmail"]

        user_detail, created = UserDetail.objects.get_or_create(user=user_obj)
        user_detail.ava.save(request.POST["inputLoadPic"], request.FILES, save=False)
        user_detail.about = request.POST["inputAbout"]

        user_detail.save()
        user_obj.save()

        return HttpResponseRedirect(reverse('login:edit'), {'success_message': 'Data has been successfully saved'})
    except:
        error_message = "Have error"
    return HttpResponseRedirect(reverse("login:edit"), {'error_message': error_message})'''


def user_logout(request):
    auth.logout(request)
    return redirect(get_referer_view(request))
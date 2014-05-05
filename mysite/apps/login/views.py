from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from get_referer import get_referer_view

from apps.cookies.models import Cookie, Review
from apps.login.forms import UserMultiForm


def user_login(request):
    template = 'login/login.html'

    if request.method == "POST":
        if request.user.is_anonymous():
            try:
                username = request.POST['inputUserName']
                password = request.POST['inputPassword']
                user = auth.authenticate(username=username, password=password)

                if user and user.is_active:
                    auth.login(request, user)
                    return redirect(get_referer_view(request))
            except:
                messages.error(request, 'You have mistake.')
    return render_to_response(template, RequestContext(request))


def create(request):
    template = 'login/create.html'
    form = UserCreationForm()

    if request.method == "POST" and not request.user.id:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect(reverse("login:user_login"))
    elif request.user.id:
        messages.success(request, 'You have already registered')
    return render_to_response(template,
                              {'form': form},
                              RequestContext(request))


def profile(request, user_name):
    user_obj = get_object_or_404(User, username=user_name)

    best_cookies = Cookie.objects.best_for_user(user_obj)
    latest_reviews = Review.objects.latest_review(user_obj)

    context = {'user_data': user_obj,
               'best_cookies': best_cookies,
               'latest_reviews': latest_reviews
               }
    return render_to_response('login/profile.html',
                              context,
                              RequestContext(request))


@login_required(redirect_field_name=None)
def edit(request):
    form = UserMultiForm(instance=request.user)
    if request.method == 'POST':
        form = UserMultiForm(request.POST,
                             request.FILES,
                             instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data has been saved')
            return redirect(reverse('login:edit'))

    return render_to_response('login/edit.html',
                              {'form': form},
                              RequestContext(request))


def user_logout(request):
    auth.logout(request)
    return redirect(get_referer_view(request))

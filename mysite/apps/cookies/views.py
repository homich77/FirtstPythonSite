from django.contrib import messages
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from get_referer import get_referer_view

from apps.cookies.models import Cookie
from apps.cookies.forms import ReviewForm


def search(request):
    template = "cookies/index.html"
    cookies_list = Cookie.objects.all()

    if request.method == 'POST' \
            and 'search_cookie' in request.POST\
            and request.POST['search_cookie']:

        search_cookie = request.POST['search_cookie']
        cookies_list = cookies_list.filter(name__icontains=search_cookie)
    return render_to_response(template,
                              {'cookies_list': cookies_list},
                              RequestContext(request))


def detail(request, pk):
    cookie = Cookie.objects.get(pk=pk)
    user_cookie = None
    if request.user.is_authenticated():
        user_cookie = cookie.review_set.filter(user_id=request.user)
    context = {
        'cookie': cookie,
        'user_cookie': user_cookie,
        'form_review': ReviewForm()
    }
    return render_to_response('cookies/detail.html', context,
                              RequestContext(request))


def vote(request, cookie_id):
    cookie_obj = get_object_or_404(Cookie, pk=cookie_id)
    form = ReviewForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save(request.user, cookie_obj)
            messages.success(request, 'Your vote has been added')
        else:
            messages.error(request, form.errors)
    return redirect(get_referer_view(request))

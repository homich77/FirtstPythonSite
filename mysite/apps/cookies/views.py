from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.views import generic

from apps.cookies.models import Cookie

def search(request):
    template = "cookies/index.html"
    if 'search_cookie' in request.POST and request.POST['search_cookie']:
        search_cookie = request.POST['search_cookie']
        cookies_list = Cookie.objects.filter(name__icontains = search_cookie)
        #return render_to_response(template, {'cookies_list': cookies_list}, RequestContext(request))
    else:
        cookies_list = Cookie.objects.all()
    return render_to_response(template, {'cookies_list': cookies_list}, context_instance = RequestContext(request))

class DetailView(generic.DetailView):
    model = Cookie
    template_name = 'cookies/detail.html'
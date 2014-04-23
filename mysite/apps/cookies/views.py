from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.views import generic
from apps.cookies.models import Review, Cookie
from django.utils import timezone
from django.db.models import Avg

def search(request):
    template = "cookies/index.html"
    if 'search_cookie' in request.POST and request.POST['search_cookie']:
        search_cookie = request.POST['search_cookie']
        cookies_list = Cookie.objects.filter(name__icontains = search_cookie)
        #return render_to_response(template, {'cookies_list': cookies_list}, RequestContext(request))
    else:
        cookies_list = Cookie.objects.annotate(average_mark=Avg('review__mark'))
#return Cookie.objects.annotate(average_mark=Avg('review__mark')).filter(average_mark__gte=4).order_by('-average_mark')
    return render_to_response(template, {'cookies_list': cookies_list}, context_instance = RequestContext(request))

class DetailView(generic.DetailView):
    model = Cookie
    template_name = 'cookies/detail.html'

def vote(request, cookie_id):
    obj = get_object_or_404(Cookie, pk=cookie_id)
    r = Review(user_id=request.user, cookie_id=obj, text=request.POST["description"], mark=request.POST["mark"], date=timezone.now())
    r.save()
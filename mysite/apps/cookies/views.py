from django.shortcuts import get_object_or_404, render, render_to_response, HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views import generic
from django.utils import timezone
from django.db.models import Avg
from django.core.urlresolvers import reverse

from apps.cookies.models import Review, Cookie

def search(request):

    template = "cookies/index.html"
    cookies_list = Cookie.objects.annotate(average_mark=Avg('review__mark'))

    if request.method == 'POST' and \
        'search_cookie' in request.POST and request.POST['search_cookie']:

        search_cookie = request.POST['search_cookie']
        cookies_list = Cookie.objects.filter(name__icontains = search_cookie)
    return render_to_response(template, {'cookies_list': cookies_list}, context_instance = RequestContext(request))


class DetailView(generic.DetailView):
    model = Cookie
    template_name = 'cookies/detail.html'

    def get_queryset(self):
        return Cookie.objects.annotate(avg_mark=Avg('review__mark'))


def vote(request, cookie_id):
    #if request.method == 'POST':
    cookie_obj = get_object_or_404(Cookie, pk=cookie_id)

    mark = request.POST["mark"]
    #TODO: validate mark
    #if mark > 5
    r = Review(user_id=request.user, cookie_id=cookie_obj, text=request.POST["description"], mark=mark, date=timezone.now())
    r.save()
    return HttpResponseRedirect(reverse('cookies:detail', args=(cookie_obj.id,)))
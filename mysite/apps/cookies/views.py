from django.shortcuts import get_object_or_404, render
from django.views import generic
from apps.cookies.models import Cookie

class IndexView(generic.ListView):
    template_name = 'cookies/index.html'
    context_object_name = 'cookies_list'

    def get_queryset(self):
        return Cookie.objects.all()
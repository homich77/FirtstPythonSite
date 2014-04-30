from django.shortcuts import redirect
from django.views import generic
from apps.cookies.models import Cookie


class IndexView(generic.ListView):

    template_name = 'main/main.html'
    context_object_name = 'best_cookie_list'

    def get_queryset(self):
        return Cookie.objects.best()

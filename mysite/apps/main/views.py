from django.shortcuts import redirect
from django.views import generic
from apps.cookies.models import Cookie
from django.db.models import Avg


class IndexView(generic.ListView):

    template_name = 'main/main.html'
    context_object_name = 'best_cookie_list'

    def get_queryset(self):
        return Cookie.objects.annotate(average_mark=Avg('review__mark')).filter(average_mark__gte=4).order_by('-average_mark')
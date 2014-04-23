from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect
from apps.cookies.models import Cookie, Review
from django.db.models import Avg


class IndexView(generic.ListView):
    template_name = 'main/main.html'
    context_object_name = 'best_cookie_list'

    def get_queryset(self):
        return Cookie.objects.annotate(average_mark=Avg('review__mark')).filter(average_mark__gte=4).order_by('-average_mark')

''''
from django.contrib import auth
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template

def user_login_view(request):
    form = UserLoginForm(request.POST or None)
    context = { 'form': form, }
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return redirect('index_page')
    return direct_to_template(request, 'form.html', context)'''
from django.conf.urls import patterns, url
from apps.cookies import views

urlpatterns = patterns(
    '',
    url(r'^$', views.search, name='search'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<cookie_id>\d+)/vote/$', views.vote, name='vote'),
)

#?next=/login/edit/
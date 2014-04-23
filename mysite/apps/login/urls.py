from django.conf.urls import patterns, url
from apps.login import views

urlpatterns = patterns('',
    url(r'^$', views.user_login, name='user_login'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^out$', views.user_logout, name='user_logout')
)

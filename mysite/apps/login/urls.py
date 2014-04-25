from django.conf.urls import patterns, url
from apps.login import views

urlpatterns = patterns('',
    url(r'^$', views.user_login, name='user_login'),
    url(r'^(?P<user_name>[\w.@+-]+)/profile/$', views.profile, name='profile'),
    url(r'^edit/$', views.edit_view, name='edit'),
    url(r'^create/$', views.create, name='create'),
    #url(r'^create_save/$', views.create_save, name='create_save'),
    url(r'^save/$', views.edit_save, name='save'),
    url(r'^out$', views.user_logout, name='user_logout')
)

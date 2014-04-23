from django.conf.urls import patterns, url
from apps.main import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='main_view')
)

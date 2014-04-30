from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

#from apps.main import views as m_views
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('apps.main.urls', namespace='main')),
    url(r'^cookies/', include('apps.cookies.urls', namespace="cookies")),
    url(r'^polls/', include('apps.polls.urls', namespace="polls")),
    url(r'^login/', include('apps.login.urls', namespace="login")),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

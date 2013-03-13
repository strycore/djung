"""Root URLconf"""
from django.conf import settings
from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('main.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)$', 'serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

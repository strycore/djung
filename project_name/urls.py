"""Root URLconf"""
from django.conf import settings
from django.urls import path, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
]


# if settings.DEBUG:
#     urlpatterns += [
#         path(r'^media/(?P<path>.*)$', 'serve',
#          {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#     ]

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login', auth_views.login, {
        'template_name': 'accounts/login.html'
    }, name="accounts_login"),
    url(r'^logout', auth_views.logout, {
        'template_name': 'accounts/logout.html'
    }, name="accounts_logout"),
    url(r'^register', views.register, name="accounts_register"),
]

from django.urls import path
from core.views import home

urlpatterns = [
    path(r'', home, name="home"),
]

from django.conf.urls import url
from django.urls import path
from .views import searchView


app_name = 'search'

urlpatterns = [
    path('',searchView,name='query'),
]
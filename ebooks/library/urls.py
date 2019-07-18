from django.urls import path
from .views import AllBooksList


app_name = 'library'

urlpatterns = [
    path('',AllBooksList.as_view(),name='allbooks'),
]
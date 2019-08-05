from django.urls import path
from .views import AllBooksList,download_view,catrom_view,catcrime_view,catdet_view,catdrama_view,catfan_view


app_name = 'library'

urlpatterns = [
    path('',AllBooksList.as_view(),name='allbooks'),
    path('download/<int:book_id>',download_view,name='download'),
    path('catrom/', catrom_view,name='catrom'),
    path('catcrime/',catcrime_view,name='catcrime'),
    path('catdet/',catdet_view,name='catdet'),
    path('catdrama/',catdrama_view,name='catdrama'),
    path('catfantasy/',catfan_view,name='catfan'),

]
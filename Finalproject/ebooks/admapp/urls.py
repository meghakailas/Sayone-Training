from django.urls import path
from .views import addbooks_view, DeleteBooksView,deletebooks_view,AdminBooksList

app_name = 'admapp'
urlpatterns = [
    path('addbooks/',addbooks_view,name='addbooks'),
    path('deletebooks/',deletebooks_view,name='deletebooks'),
    path('deletebooks/<int:pk>', DeleteBooksView.as_view(), name='deletebooksconfirm'),
    path('adminbooklist/',AdminBooksList.as_view(),name='allbooksadmin'),

]
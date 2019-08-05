from django.conf.urls import url
from django.urls import path,include
from register import views

app_name = 'register'
urlpatterns = [
    path('registeruser/',views.register,name='registeruser'),
    path('user_login',views.user_login,name='user_login'),
    path('useradmin/',views.user_login,name='adminpage'),


]

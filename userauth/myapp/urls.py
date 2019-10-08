from django.urls import path
from . import views

# TEMPLATE URLS
app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('user_login', views.user_login, name='user_login'),
    path('special', views.special, name='special'),
]

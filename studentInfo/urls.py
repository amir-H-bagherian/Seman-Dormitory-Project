from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='index'),
    path('homepage/', views.home_page, name='homepage'),
]
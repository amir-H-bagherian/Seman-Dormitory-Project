from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='index'),
    path('homepage/', views.home_page, name='homepage'),
    path('farzanegan/', views.farzanegan_page, name='farzanegan'),
    path('farhikhtegan/', views.farhikhtegan_page, name='farhikhtegan'),
    path('kosar/', views.kosar_page, name='kosar'),
]
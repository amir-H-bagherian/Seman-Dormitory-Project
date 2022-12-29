from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login_user, name='index'),
    path('homepage/', views.home_page, name='homepage'),
    path('farzanegan/', views.farzanegan_page, name='farzanegan'),
    path('farhikhtegan/', views.farhikhtegan_page, name='farhikhtegan'),
    path('kosar/', views.kosar_page, name='kosar'),
    path('pre-exam/', views.pre_exam_page, name='pre-exam'),
    
    path('mbti_test/', include('mbti_test.urls')),
]

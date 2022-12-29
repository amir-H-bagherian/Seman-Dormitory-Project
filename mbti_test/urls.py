from django.urls import path
from . import views

urlpatterns=[
    path('', views.mbti_test, name='mbti_test'),
    path('mbti_result/', views.mbti_test, name='mbti_result'),
]

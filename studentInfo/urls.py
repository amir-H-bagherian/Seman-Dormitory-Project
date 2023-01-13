from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login_user, name='index'),
    path('homepage/', views.home_page, name='homepage'),
    path('farzanegan/', views.farzanegan_page, name='farzanegan'),
    path('farhikhtegan/', views.farhikhtegan_page, name='farhikhtegan'),
    path('kosar/', views.kosar_page, name='kosar'),
    path('pre-exam/', views.pre_exam_page, name='pre-exam'),
    
    path('submit_user_type/', views.submit_user_type, name='submit-user-type'),
    path('behavior_test/', views.behavior_test_page, name='behavior-test'),
    
    path('disabled/', views.disabled_request_page, name='disabled'),
    path('request-shared-room/', views.shared_room, name='request-shared-room'),
    
    path('process-user-lifestyle/', views.process_user_lifestyle, name='process-user-lifestyle'),
    
    path('mbti_test/', include('mbti_test.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home , name='home'),
    path('signup/', views.user_signup , name='signup'),
    path('login/', views.user_login , name='login'),
    path('deshbord/', views.user_deshbord , name='deshbord'),   
    path('change_pass_with_old_pass/', views.change_pass_with_old_pass , name='change_pass_with_old_pass'),
    path('change_pass_without_old_pass/', views.change_pass_without_old_pass , name='change_pass_without_old_pass'),
    path('logout/', views.user_login , name='logout'),
    path('user_details/<int:id>',views.user_details,name='user_details'),



   


]
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # نستخدم دوال العرض الجاهزة من جانغو لتسجيل الدخول والخروج
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # روابط مخصصة سنقوم ببنائها
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
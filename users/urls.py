from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
from django.urls import path, include
from django.contrib.auth import views as auth_views

from scanner import views

urlpatterns = [
    path('restrictions/', views.restrictions, name='restrictions'),
]
from django.urls import path

from scanner import views

urlpatterns = [
    path('scan/', views.scan, name='scan'),
]
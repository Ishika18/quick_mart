"""quick_mart URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from scanner.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # user auth urls
    path('', include('users.urls')),
    path('', include('scanner.urls')),
]

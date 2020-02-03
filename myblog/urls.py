from django.contrib import admin
from django.urls import path
from .views import index, serve_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('data/', serve_data)
]

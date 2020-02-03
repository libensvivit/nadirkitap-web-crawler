from django.urls import path
from .views import index, serve_data

urlpatterns = [
    path('', index),
    path('data', serve_data)
]

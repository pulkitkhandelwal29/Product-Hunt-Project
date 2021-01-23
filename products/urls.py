from django.urls import path, include

# Importing the views.py file of the products app
from . import views


urlpatterns = [
    path('create', views.create, name='create'),
]

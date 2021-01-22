from django.urls import path, include

# Importing the views.py file of the accounts app
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]

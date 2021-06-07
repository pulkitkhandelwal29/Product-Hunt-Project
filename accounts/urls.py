from django.urls import path, include

# Importing the views.py file of the accounts app
from . import views

#It is the request coming from the main "urls.py" file to the accounts "urls.py" file.
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]

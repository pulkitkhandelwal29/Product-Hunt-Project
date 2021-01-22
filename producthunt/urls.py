from django.contrib import admin
from django.urls import path,include

#Importing the views.py file of the products app
from products import views



urlpatterns = [
    path('admin/', admin.site.urls),
    #for the homepage
    path('',views.home,name='home'),
    #include the urls.py of accounts app
    path('accounts/',include('accounts.urls')),
]

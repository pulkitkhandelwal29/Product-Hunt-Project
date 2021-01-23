from django.contrib import admin
from django.urls import path,include

#Importing the views.py file of the products app
from products import views

#This is the settings.py containing information about the MEDIA_URL and MEDIA_ROOT
from django.conf import settings

#Helps to work with the static files
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    #for the homepage
    path('',views.home,name='home'),
    #include the urls.py of accounts app
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

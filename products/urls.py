from django.urls import path, include

# Importing the views.py file of the products app
from . import views


urlpatterns = [
    path('create', views.create, name='create'),
    #for detail of the product, it will appear like /products/1
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]

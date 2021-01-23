from django.contrib import admin

# Referring to current directory i.e. product(the class name) import from its models.py
from .models import Product

#register the class to get it appeared on the admin page.
#If u do not want any model to appear on Admin Page, then don't register here
#By registering Product will appear on admin Page
admin.site.register(Product)

from django.shortcuts import render,redirect

#Package for action only when user is logged in
from django.contrib.auth.decorators import login_required

#Creation of products
from .models import Product

#Package for timezone
from django.utils import timezone

def home(request):
    return render(request,'products/home.html')

#When the user goes to create page, it must be logged in otherwise this will show 404 error or we can move to other page(custom)
@login_required
def create(request):
    if request.method == 'POST':
        #Checking if the request contains these things or not
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            #Creating an object
            product=Product()

            #Now assigning values
            product.title = request.POST['title']
            product.body = request.POST['body']

            #checking of url if it contains http or https at starting otherwise we will append it
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']

            #Icon and images
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']

            #Adding pub_date automatically (not taking from user)
            product.pub_date = timezone.datetime.now()

            #votes_total is already set to 1, we do not have to set it again (it is set in the database)

            #Setting the User
            product.hunter = request.user

            #saving into the database
            product.save()

            return redirect('home')

        else:
            return render(request,'products/create.html',{'error':'All fields are required'})
    else:
        return render(request,'products/create.html')

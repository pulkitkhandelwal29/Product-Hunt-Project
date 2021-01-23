from django.shortcuts import render,redirect, get_object_or_404

#Package for action only when user is logged in
from django.contrib.auth.decorators import login_required

#Creation of products
from .models import Product

#Package for timezone
from django.utils import timezone

#setting up the homepage
def home(request):
    products = Product.objects
    return render(request,'products/home.html',{'products':products})

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

            #returning to the /products/2       (eg--inserted product id)
            return redirect('/products/' + str(product.id))

        else:
            return render(request,'products/create.html',{'error':'All fields are required'})
    else:
        return render(request,'products/create.html')


def detail(request,product_id):
    #getting objects from get_object_or_404
    #Find object using the primary key and if the object is not there, 404 error
    product=get_object_or_404(Product,pk = product_id)
    #will pass product object to html
    return render(request,'products/detail.html',{'product':product})


#function for Upvote
#This will require login, and if it is not login, will redirect to login page
@login_required(login_url='/accounts/login')
def upvote(request,product_id):
    if request.method == 'POST':
        product=get_object_or_404(Product,pk = product_id)
        product.votes_total +=1
        product.save()
        return redirect('/products/' + str(product.id))

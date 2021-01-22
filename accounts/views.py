from django.shortcuts import render,redirect

#Authentication files
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    #User has info and wants an account now!
    if request.method=="POST":
        #Will check the password and then check whether this user exists or not
        if request.POST['password1'] == request.POST['password2']:
            try:
                #check whether this username that wants to sign up exists or not
                user = User.objects.get(username = request.POST['username'])
                #If the username is same, then we will give an error on the signup page only
                return render(request,'accounts/signup.html',{'error':'Username already exists'})
            #if the usernames does not exist, we will create a user
            except User.DoesNotExist:
                #Creating user
                user = User.objects.create_user(request.POST['username'],request.POST['password1'])
                #Particular user being registered
                auth.login(request,user)
                #If the user has signed up, redirect it to the homepage(need to import redirect)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'Passwords must Match'})
    else:
        #User wants to enter info
        return render(request,'accounts/signup.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return render(request,'accounts/signup.html')

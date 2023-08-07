from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from  django.contrib import messages
# Create your views here.

def auth(request):
    return render(request, "auth-home.html")

def login(request):
    
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if User.check_password == password:
            print("User.email:  ",  User.email)
            messages.success(request, "you have been logedin successfully")
            return redirect(request,"/home")
    return render(request, "login.html")


def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        newUser = User(username=username, email=email, password=password1)
        newUser.firstname = firstname
        newUser.lastname = lastname      

        newUser.save()  

        messages.success(request, "your account has been created successfully")
       
        
    return render(request, "signup.html")

    


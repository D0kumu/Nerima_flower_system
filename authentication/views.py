from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from  django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def auth(request):
    return render(request, "authentication/auth-home.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'main/home.html', {"fname": fname})
        else:
            messages.error(request, "You entered bad credentials!!")
    return render(request, "authentication/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        newUser = User.objects.create_user(username,email, password1)
        newUser.first_name = firstname
        newUser.last_name = lastname      

        newUser.save()
        login(request, newUser)
        messages.success(request, "your account has been created successfully")
        return redirect('/auth')
    return render(request, "authentication/signup.html")

def signout(request):
    logout(request)
    messages.success(request, "you are logged out successfully")
    return redirect('home')


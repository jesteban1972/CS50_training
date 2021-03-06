from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def index(request):
    if not request.user.is_authenticated: # If no user is signed in, return to login page
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/index.html")

def login_view(request):
    if request.method == "POST": # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password) # Check if username and password are correct, returning User object if so
        
        if user: # If user object is returned, log in and route to index page
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else: # Otherwise, return login page again with new context
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out"
    })
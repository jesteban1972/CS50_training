from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#     return HttpResponse("<h1 style=\"color:blue\">This is my first Python & Django web app</h1>")

def index(request):
    return render(request, "first_app/index.html")

def javier(request):
    return HttpResponse("Hello, Javier!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "first_app/greet.html", {
        "name": name.capitalize()
    })
from django.shortcuts import render

def index(request):
    return render(request, "forms/index.html")

def add(request):
    return render(request, "forms/add.html")
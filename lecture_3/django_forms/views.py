from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

#ws (without sessions)
#ws tasks = ["write a report", "post report to boss", "relaxing"]

#def index(request):
#    return render(request, "django_forms/index.html", {
#        "tasks": tasks
#    })

def index(request):

    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "django_forms/index.html", {
        "tasks": request.session["tasks"]
    })
    
def test(request):
    return render(request, "django_forms/test.html")

def add(request):

    django_form = NewTaskForm(request.POST) # Take in the data the user submitted and save it as form

    if request.method == "POST":
    
        #django_form = NewTaskForm(request.POST) # Take in the data the user submitted and save it as form
        
        if django_form.is_valid():
            task = django_form.cleaned_data["task"] # Isolate the task from the 'cleaned' version of form data
            #ws tasks.append(task) # Add the new task to our list of tasks
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("django_forms:index")) # Redirect user to list of tasks
        
    else: # If the form is invalid, re-render the page with existing information.
        return render(request, "django_forms/add.html", {
            "django_form": django_form
        })
        
    return render(request, "django_forms/add.html", {
        "django_form": NewTaskForm()
    })

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
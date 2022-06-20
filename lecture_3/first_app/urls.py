from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("javier", views.javier, name="javier"),
    path("<str:name>", views.greet, name="greet")
]
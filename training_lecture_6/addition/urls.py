from django.urls import path
from . import views

app_name = "addition"

urlpatterns = [
    path("", views.index, name="index"),
]
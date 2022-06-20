from django.urls import path
from . import views

app_name = "django_forms"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("test", views.test, name="test")
]
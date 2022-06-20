from django.urls import path
from . import views

app_name = "styles"
urlpatterns = [
    path("", views.index, name="index")
]
from django.urls import include, path
from . import views

app_name = "home"

urlpatterns = [
    path("home/", views.home, name="home"),
]

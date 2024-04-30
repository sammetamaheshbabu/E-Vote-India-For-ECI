from xml.etree.ElementInclude import include
from django.urls import path
from . import views

app_name = "polling"

urlpatterns = [
    path("polling/", views.polling_page, name="polling_page"),
]

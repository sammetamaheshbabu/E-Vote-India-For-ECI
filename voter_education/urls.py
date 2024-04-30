from django.urls import path
from . import views

urlpatterns = [
    path("voter_education/", views.voter_education, name="voter_education"),
]

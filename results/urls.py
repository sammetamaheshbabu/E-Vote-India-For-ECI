from django.urls import path
from . import views

urlpatterns = [
    path("results/", views.party_results, name="results"),
]

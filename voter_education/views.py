from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def voter_education(request):
    template = loader.get_template("voter_education.html")
    return HttpResponse(template.render())

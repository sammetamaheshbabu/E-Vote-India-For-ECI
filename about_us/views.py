from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def about_us(request):
    template = loader.get_template("about_us.html")
    return HttpResponse(template.render())

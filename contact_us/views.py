from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def contact_us(request):
    template = loader.get_template("contact_us.html")
    return HttpResponse(template.render())

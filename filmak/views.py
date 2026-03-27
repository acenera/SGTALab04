from unittest import loader

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def register(request):
    template = loader.get_template("filmak/erregistratu.html")
    return HttpResponse(template.render(request))


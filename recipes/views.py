from django.shortcuts import render
from django.http import HttpResponse

def recipes(request):
    return HttpResponse("Hello, world. You're the recipes.")

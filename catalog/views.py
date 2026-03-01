from django.shortcuts import render
from django.http import HttpResponse

def catalog(request):
    return HttpResponse("Hello, world. You're the catalog.")

from django.shortcuts import render
from django.http import HttpResponse

def reviews(request):
    return HttpResponse("Hello, world. You're the reviews")

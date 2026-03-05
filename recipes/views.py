from django.shortcuts import render
from django.http import HttpResponse

def recipes(request):
    return HttpResponse("Hello, world. You're the recipes.")

"""
from django.shortcuts import render

def supply(request):
    context = {}
    # Make sure to create supply/templates/supply/index.html for this to work
    return render(request, 'supply/index.html', context)
"""
from django.shortcuts import render
from django.http import HttpResponse
def restaurants(request):
    return HttpResponse("Hello, world. You're the restaurants")
# Create your views here.

"""
from django.shortcuts import render

def supply(request):
    context = {}
    # Make sure to create supply/templates/supply/index.html for this to work
    return render(request, 'supply/index.html', context)
"""
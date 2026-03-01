from django.shortcuts import render
from django.http import HttpResponse
def accounts(request):
    return HttpResponse("This is the accounts page")
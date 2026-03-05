from accounts.forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User

def accounts(request):
    return HttpResponse("Hello, world. You're at the account page.")



def user_profile(request, username):
    # find the profile of user or feedback 404 not found
    profile_user = get_object_or_404(User, username=username)

    context_dict = {'profile_user': profile_user}
    return render(request, 'accounts/profile.html', context_dict)



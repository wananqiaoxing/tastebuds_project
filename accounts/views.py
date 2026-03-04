from accounts.forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User

def accounts(request):
    return HttpResponse("Hello, world. You're at the account page.")

def register(request):
    # register status
    registered = False

    if request.method == 'POST':
        #request
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        # check the form
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            # save UserProfile form
            profile = profile_form.save(commit=False)
            profile.user = user

            profile_path = reverse('accounts:profile', kwargs={'username': user.username})
            profile.website = request.build_absolute_uri(profile_path)
            # user connect to froflie
            profile.user = user

            # deal with picture
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # save profile
            profile.save()

            registered = True
        else:
            #wrong
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request, 'accounts/register.html', context_dict)

def user_login(request):
    context_dict = {}

    if request.method == 'POST':
        # acquire username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check the user
        user = authenticate(username=username, password=password)

        if user:
            # if user is active
            if user.is_active:
                # login
                login(request, user)
                # return to the main page
                return redirect('accounts:profile', username=user.username)
            else:
                context_dict['error_msg'] = "Your tastebuds account is disabled."
        else:
            # error
            context_dict['error_msg'] = "user name or password is incorrect."

    # No context variables to pass to the template system, hence the blank dictionary object
    return render(request, 'accounts/login.html', context_dict)


def user_logout(request):
    logout(request)
    return redirect('main')


def user_profile(request, username):
    # find the profile of user or feedback 404 not found
    profile_user = get_object_or_404(User, username=username)

    context_dict = {'profile_user': profile_user}
    return render(request, 'accounts/profile.html', context_dict)



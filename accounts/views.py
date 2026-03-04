from django.shortcuts import render, redirect
from accounts.forms import UserForm, UserProfileForm
from django.http import HttpResponse

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



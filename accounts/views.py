from accounts.forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import UserProfile


def accounts(request):
    return HttpResponse("Hello, world. You're at the account page.")



def user_profile(request, username):
    # find the profile of user or feedback 404 not found
    profile_user = get_object_or_404(User, username=username)
    # 在这里确保 UserProfile 一定存在（关键位置）
    UserProfile.objects.get_or_create(user=profile_user)
    # 用户收藏的食谱（Bookmark 区域需要）
    bookmarks = profile_user.userprofile.bookmarks.all() if hasattr(profile_user, 'userprofile') else None
    # 用户评论（My reviews 区域需要）
    reviews = profile_user.reviews.all()
    # 用户提交的所有食谱（Submission 区域需要）
    submitted_recipes = profile_user.recipes.all()

    context_dict = {
        'profile_user': profile_user,
        'bookmarks': bookmarks,
        'reviews': reviews,
        'submitted_recipes': submitted_recipes,
    }

    return render(request, 'accounts/profile.html', context_dict)

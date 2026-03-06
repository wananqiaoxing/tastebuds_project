from django.urls import path
from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('profile/<str:username>/', views.user_profile, name='profile'),
]
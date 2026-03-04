from django.urls import path
from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('register', views.register, name='register'),
]
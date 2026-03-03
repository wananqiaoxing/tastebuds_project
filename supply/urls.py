from django.urls import path
from supply import views

app_name = 'supply'
urlpatterns = [
    path('', views.supply, name='supply'),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='events'),
    path('accounts/profile/', views.profile, name="profile"),
]
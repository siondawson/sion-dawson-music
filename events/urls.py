from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='events'),
    path('accounts/profile/', views.profile, name="profile"),
    path('all-events/', views.all_events, name='all-events'),
    path('event/<int:event_id>/', views.event_detail, name='event-detail'),
]
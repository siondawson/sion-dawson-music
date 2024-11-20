from django.contrib import admin
from django.urls import path, include
from events import views  # Import index view from events app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('events/', include('events.urls')),  # Include events app URLs
    path('', views.index, name='home'),  # Map the root URL to the events app's index view
    path('accounts/profile/', views.profile, name="profile"),  # Profile route
]

from django.shortcuts import render

def index(request):
    """A view to return the index page"""

    return render(request, 'events/index.html')


def profile(request):
    return render(request, 'profile.html')

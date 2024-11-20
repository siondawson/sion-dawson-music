from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Event, BandName
from django.contrib.auth.models import User

def index(request):
    """A view to return the index page"""

    return render(request, 'events/index.html')


def profile(request):
    return render(request, 'profile.html')





def all_events(request):
    # Fetch all events from the database
    events = Event.objects.all()

    # Prepare the context
    context = {
        'events': events,
    }

    # Return the rendered template with context
    return render(request, 'all-events.html', context)


def event_detail(request, event_id):
    # Fetch the event, including related slots
    event = get_object_or_404(Event, id=event_id)
    
    # Pass the event and slots to the template
    return render(request, 'events/event-detail.html', {
        'event': event,
        'slots': event.slots.all(),  # Use the 'slots' reverse relationship
    })
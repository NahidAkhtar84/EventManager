from django.shortcuts import render
from event_booking.models import Events

# Create your views here.

def Index(request):
    all_events = Events.objects.filter(status='accepted')
    context = {
        "events": all_events,
    }
    return render(request, 'index/index.html', context)

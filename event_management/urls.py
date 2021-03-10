
from django.contrib import admin
from django.urls import path
from event_booking.views import calendar

urlpatterns = [
    #user View
    path('calendar/', calendar, name='calendar'),
    # DJ Admin Section
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from event_booking.views import add_event, EventBook, update, remove

urlpatterns = [
    # user View
    # path('calendar/', calendar, name='calendar'),
    path('add_event$', add_event, name='add_event'),
    path('eventbookingpage', EventBook.as_view(), name='eventbookingpage'),
    path('booking', EventBook.as_view(), name='booking'),
    path('update$', update, name='update'),
    path('remove', remove, name='remove'),

    # DJ Admin Section
    path('admin/', admin.site.urls),

    # custom admin
    path('admin-site/', include('admin_site.urls')),
    path('', include('blog.urls')),
]

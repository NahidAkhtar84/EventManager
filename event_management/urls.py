from django.contrib import admin
from django.urls import path, include
from event_booking.views import calendar

urlpatterns = [
    # user View
    path('calendar/', calendar, name='calendar'),
    # DJ Admin Section
    path('admin/', admin.site.urls),
    # custom admin
    path('admin-site/', include('admin_site.urls')),
    path('', include('blog.urls')),
]

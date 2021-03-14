from django.urls import path
from . import views
from event_booking import views as event_views

urlpatterns = [
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('write-post/', views.WritePost, name='write-post'),
    path('manage-post/', views.ManagePost, name='manage-post'),
    path('edit-post/<str:pk>', views.EditPost, name='edit-post'),
    path('delete-post/<str:pk>', views.DeletePost, name='delete-post'),

    # Events Page
    path('event-requests/', event_views.EventRequests, name='all-events'),
    path('event/accept/<str:pk>', event_views.AcceptEvent, name='accept'),
    path('event/reject/<str:pk>', event_views.RejectEvent, name='reject'),
    path('event/edit/<str:pk>', event_views.EditEvent, name='edit-event'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('write-post/', views.WritePost, name='write-post'),
    path('manage-post/', views.ManagePost, name='manage-post'),
    path('edit-post/<str:pk>', views.EditPost, name='edit-post'),
    path('delete-post/<str:pk>', views.DeletePost, name='delete-post'),
]

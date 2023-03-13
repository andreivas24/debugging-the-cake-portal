from django.urls import path
from notifications.views import show_notifications

urlpatterns = [
    path('', show_notifications, name='show-notifications'),


]

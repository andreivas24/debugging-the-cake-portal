from django.urls import path

from chats.views.chatrooms_view import chatrooms_view
from chats.views.room_view import room_view

urlpatterns = [
    path('chatrooms/', chatrooms_view, name='chatrooms'),
    path('<slug:slug>/', room_view, name='room'),
]
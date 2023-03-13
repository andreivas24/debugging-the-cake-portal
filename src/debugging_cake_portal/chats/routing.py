from django.urls import path

from chats import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatRoomConsumer.as_asgi()),
]
from django.contrib import admin
from chats.models.chatroom_model import ChatRoom
from chats.models.message_model import Message

admin.site.register(ChatRoom)
admin.site.register(Message)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chats.models.chatroom_model import ChatRoom
from chats.models.message_model import Message


@login_required
def room_view(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'chats/room.html', {
        'room': room,
        'messages': messages
    })

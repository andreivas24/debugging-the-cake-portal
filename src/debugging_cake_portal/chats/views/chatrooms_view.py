from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chats.models.chatroom_model import ChatRoom


@login_required()
def chatrooms_view(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chats/chatrooms.html', {
        "rooms": rooms
    })

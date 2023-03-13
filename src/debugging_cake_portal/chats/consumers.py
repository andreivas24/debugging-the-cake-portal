import os
from os.path import exists
import json
from cake_user.models.user_model import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from chats.models.chatroom_model import ChatRoom
from chats.models.message_model import Message


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        # room = event['room']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            # 'room': room
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message)

        latest_message = Message.objects.latest('id')
        save_path = r'/data/debugging_cake/input/'
        relative_path = r'%s/%s/messages' % (user.username, room.name)
        full_path = os.path.join(save_path, relative_path)

        if exists(full_path):
            file_name = os.path.join(full_path, 'user_messages.txt')
            with open(file_name, 'a+') as file:
                file.write(latest_message.content + "\n")
                file.close()
        else:
            os.makedirs(full_path)
            file_name = os.path.join(full_path, 'user_messages.txt')
            with open(file_name, 'a+') as file:
                file.write(latest_message.content + "\n")
                file.close()

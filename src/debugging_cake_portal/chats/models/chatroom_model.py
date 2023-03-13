from django.db import models


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Chatroom {self.name}"

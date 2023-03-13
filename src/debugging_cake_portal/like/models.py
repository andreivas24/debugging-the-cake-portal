import datetime
from django.db import models
from cake_user.models.user_model import User
from posts.models.post_model import Post


class Like(models.Model):
    liked = 'Like'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    value = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"

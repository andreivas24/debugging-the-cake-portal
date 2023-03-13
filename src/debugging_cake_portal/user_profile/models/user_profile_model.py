from django.db import models
from cake_user.models.user_model import User
from posts.models.post_model import Post
from tag.models.tag_model import Tag
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    _full_name = models.CharField(max_length=100, blank=True, null=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    about_me = models.TextField(max_length=140, blank=True, null=False)
    posts = models.ForeignKey(Post, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # will run the save method of the parent class
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        # will resize the image and save it back at the same path with the new size of 300x300 px
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

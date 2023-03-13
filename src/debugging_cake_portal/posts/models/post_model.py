from django.db import models
from django.utils import timezone
from cake_user.models.user_model import User
from debugging_cake_portal.settings import num_for_prev
from tag.models.tag_model import Tag
from django.urls import reverse


def get_upload_to(instance, filename):
    return 'upload/%s/post%s/%s' % (instance.author.username, instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    updated = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post_tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to=get_upload_to, blank=True, null=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return f"{self.author}'s post in {self.post_tag}"

    @property
    def results(self):
        file = self.file.path
        data_file = open(file, 'r')
        data = data_file.read(num_for_prev)
        return data

    @property
    def num_likes(self):
        return self.liked.all().count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_file = self.file
            self.file = None
            super(Post, self).save(*args, **kwargs)
            self.file = saved_file
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super().save(*args, **kwargs)

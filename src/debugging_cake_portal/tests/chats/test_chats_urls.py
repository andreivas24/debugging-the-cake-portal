import pytest
from django.urls import reverse, resolve
from chats.views import chatrooms_view, room_view
from posts.views import PostListView


class TestUrls:

    def test_chatrooms_url_is_resolved(self):
        url = reverse('chatrooms')
        assert resolve(url).func, chatrooms_view

    def test_room_url_is_resolved(self):
        url = reverse('room', args=['slug'])
        assert resolve(url).func, room_view

    def test_posts_url_is_resolved(self):
        url = reverse('index')
        assert resolve(url).func, PostListView

import pytest
from django.urls import reverse, resolve
import unittest

from cake_user.models import User
from posts.models import Post
from tag.models import Tag


# @pytest.mark.django_db
# class TestViews(unittest.TestCase):
#     def setUp(self):
#         self.post = Post()
#         post1 = Post.objects.create(title="TestPost1")
#
#     def test_details(self):
#         response = self.post.get(reverse('index'))
#         self.assertIn('environment', response.context)

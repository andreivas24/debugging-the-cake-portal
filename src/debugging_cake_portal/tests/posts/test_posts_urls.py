
from django.urls import reverse, resolve
import posts
from posts.views import PostListView, PostDetailView, PostCreateView


# 1) din os -> testam daca merge runserver

class TestUrls:
    def test_post_url_index_ok(self):
        url = reverse('index')
        assert(resolve(url).func, PostListView)

    def test_post_url_detail_ok(self):
        url = reverse('post-detail', args=[1])
        assert(resolve(url).func, '/posts/1')

    def test_post_url_create_ok(self):
        url = reverse('create-post')
        assert(resolve(url).func, PostCreateView)
        

# Project settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debugging_cake_portal.settings")
import django

django.setup()

from comment.models import Comment
from posts.models.post_model import Post
from cake_user.models.user_model import User
from rest_framework.test import APIRequestFactory
from rest_framework import status
import pytest, json
from ast import literal_eval

from dashboard.views import dashboard_with_pivot, pivot_data
from dashboard.models import Analysis


class TestDashboardViews:

    def test_load_admin_OK(self):
        factory = APIRequestFactory()
        request = factory.get(path="dashboard/")
        request.user = User.objects.get(username='admin')
        view = dashboard_with_pivot(request)
        assert view.status_code == status.HTTP_200_OK

    def test_load_anonymous_KO(self):
        factory = APIRequestFactory()
        request = factory.get(path="dashboard/")
        view = dashboard_with_pivot(request)
        assert view.status_code == status.HTTP_403_FORBIDDEN

    def test_API_admin_OK(self):
        factory = APIRequestFactory()
        request = factory.get(path="dashboard/")
        request.user = User.objects.get(username='admin')
        view = pivot_data(request)
        assert view.status_code == status.HTTP_200_OK

    def test_API_anonymous_KO(self):
        factory = APIRequestFactory()
        request = factory.get(path="dashboard/")
        view = pivot_data(request)
        assert view.status_code == status.HTTP_403_FORBIDDEN

    def test_check_data_OK(self):
        factory = APIRequestFactory()
        request = factory.get(path="dashboard/")
        request.user = User.objects.get(username='admin')
        view = pivot_data(request)

        dataset = [
            ['Fields', 'users', 'posts', 'comments'],
            ['moderator', User.objects.filter(roles__id=3).count(), Post.objects.filter(author__roles=3).count(),
             Comment.objects.filter(user__roles=3).count()],
            ['compo', User.objects.filter(roles__id=2).count(), Post.objects.filter(author__roles=2).count(),
             Comment.objects.filter(user__roles=2).count()],
            ['developer', User.objects.filter(roles__id=1).count(), Post.objects.filter(author__roles=1).count(),
             Comment.objects.filter(user__roles=1).count()]
        ]

        response = literal_eval(view.content.decode('utf-8'))

        assert len(response) > 0
        assert len(response) == len(dataset)
        for (expected, recieved) in zip(dataset, response):
            assert len(expected) == len(recieved)
            for (expected_value, recieved_value) in zip(expected, recieved):
                assert expected_value == recieved_value

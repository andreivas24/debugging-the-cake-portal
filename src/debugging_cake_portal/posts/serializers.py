from rest_framework import serializers
from .models import Post
from django import forms


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    instance: Post

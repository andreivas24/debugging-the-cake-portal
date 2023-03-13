from rest_framework import serializers
from tag.models.tag_model import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_type', 'color']

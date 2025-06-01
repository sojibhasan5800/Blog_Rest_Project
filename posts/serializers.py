from rest_framework import serializers
from .models import Post
from django.conf import settings
from rest_framework.response import Response

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'create_date', 'update_date']
        read_only_fields = ['create_date', 'update_date']
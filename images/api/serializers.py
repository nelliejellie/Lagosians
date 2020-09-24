from rest_framework import serializers
from ..models import Image, Comment

class ImageSerializer(serializers.ModelSerializer):
    # overriding this class with your model class
    class Meta:
        # model thats being serialized
        model = Image
        fields = ['id', 'user', 'title', 'description', 'image', 'created', 'users_like', 'total_likes']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'title', 'body', 'like', 'created', 'updated', 'image']
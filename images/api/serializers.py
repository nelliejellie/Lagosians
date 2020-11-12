from rest_framework import serializers
from ..models import Image, Comment

class ImageSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    
    # overriding this class with your model class
    class Meta:
        # model thats being serialized
        model = Image
        fields = ['id', 'username', 'title', 'description', 'image', 'created', 'users_like', 'total_likes','slug',]

    def get_username(self, Image):
        username = Image.user.username
        return username

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Comment
        fields = ['id', 'title', 'body', 'like', 'created', 'updated', 'image', 'username']

    def get_username(self, Comment):
        username = Comment.user.username
        return username
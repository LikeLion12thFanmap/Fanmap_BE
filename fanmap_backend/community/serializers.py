from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Community, Comment
from django.contrib.auth.models import User

class CommunitySerializer(ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.username') 
    
    class Meta:
        model = Community
        fields = ['id', 'title', 'content', 'created_at', 'image', 'video', 'link', 'location', 'writer']
    
class CommentSerializer(ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'writer.username') 
    
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'date', 'post', 'writer']
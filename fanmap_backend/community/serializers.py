from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Community, Comment
from accounts.models import CustomUser  

class CommunitySerializer(ModelSerializer):
    userid = serializers.ReadOnlyField(source = 'user.username') 
    nickname = serializers.ReadOnlyField(source = 'user.nickname')
    
    class Meta:
        model = Community
        fields = ['id', 'title', 'content', 'created_at', 'image', 'video', 'link', 'location', 'userid', 'nickname']
    
class CommentSerializer(ModelSerializer):
    userid = serializers.ReadOnlyField(source = 'user.username') 
    nickname = serializers.ReadOnlyField(source = 'user.nickname')
    
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'date', 'post', 'userid', 'nickname']
from django.shortcuts import render
from .models import Community, Comment
from .serializers import CommunitySerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet

class CommunityViewSet(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):  
        serializer.save(writer = self.request.user)
    
    def get_queryset(self, **kwargs):
        id = self.kwargs['community_id']
        return self.queryset.filter(post=id)

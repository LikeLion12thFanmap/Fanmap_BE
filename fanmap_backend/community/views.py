from django.shortcuts import render
from .models import Community, Comment
from .serializers import CommunitySerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CommunityViewSet(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        community = get_object_or_404(Community, pk=pk)
        user = request.user
        
        if user in community.likes.all():
            community.likes.remove(user)
            return Response({'status': 'like removed'})
        else:
            community.likes.add(user)
            return Response({'status': 'like added'})        

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):  
        serializer.save(user = self.request.user)
    
    def get_queryset(self, **kwargs):
        id = self.kwargs['community_id']
        return self.queryset.filter(post=id)

from django.shortcuts import render
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework import permissions

class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    
    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAdminUser]  # 인증된 사용자만 수정/삭제 가능

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

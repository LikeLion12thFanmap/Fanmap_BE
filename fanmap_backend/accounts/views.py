# postboxProject/ accounts/ views.py (accounts 앱 내 views.py) 

from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
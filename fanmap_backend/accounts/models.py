from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    nickname = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    favorite_star = models.CharField(max_length=128 ,null=True)
    
    # 다른 필드를 여기에 추가하세요

    def __str__(self):
        return self.username

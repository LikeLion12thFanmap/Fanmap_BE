from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    nickname = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    favorite_star = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.username

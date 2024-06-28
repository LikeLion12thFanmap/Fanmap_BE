from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    location = models.CharField(verbose_name="위치", max_length=128)
    pName = models.CharField(verbose_name="장소이름", max_length=200)
    purpose = models.CharField(verbose_name="장소 목적", max_length=128)
    sTime = models.TimeField(verbose_name="활성화시작시간", auto_now=False)
    eTime = models.TimeField(verbose_name="활성화종료시간", auto_now=False)
    basic_cate = models.CharField(verbose_name="기본카테고리", max_length=200)
    detail_cate = models.CharField(verbose_name="세부카테고리", max_length=200)
    require = models.CharField(verbose_name="필요조건", max_length=300, blank=True, null=True)
    link = models.URLField(verbose_name="링크", blank=True, null=True)
    thumbnail = models.ImageField(verbose_name="대표이미지", blank=True, null=True, upload_to='place_image')
    image1 = models.ImageField(verbose_name="이미지1", blank=True, null=True, upload_to='place_image')
    image2 = models.ImageField(verbose_name="이미지2", blank=True, null=True, upload_to='place_image')
    image3 = models.ImageField(verbose_name="이미지3", blank=True, null=True, upload_to='place_image')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.location
    
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    work_time = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    image1 = models.ImageField(verbose_name="이미지1", blank=True, null=True, upload_to='place_image')
    image2 = models.ImageField(verbose_name="이미지2", blank=True, null=True, upload_to='place_image')
    image3 = models.ImageField(verbose_name="이미지3", blank=True, null=True, upload_to='place_image')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

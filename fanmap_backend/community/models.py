from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Community(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    content = models.TextField(verbose_name="내용", default='')
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    image = models.ImageField(verbose_name="이미지1", blank=True, null=True, upload_to='image')
    video = models.FileField(verbose_name="영상", blank=True, null=True, upload_to='video')
    link = models.URLField(verbose_name="링크", blank=True, null=True)
    #location type 재설정 필요
    location = models.CharField(verbose_name="위치", max_length=128, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    #좋아요 기능
    likes = models.ManyToManyField(CustomUser, related_name='like_community')
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment = models.CharField(verbose_name="댓글", max_length=128)
    date = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    post = models.ForeignKey(Community, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment
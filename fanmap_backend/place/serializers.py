from rest_framework.serializers import ModelSerializer
from .models import Place,Restaurant
from accounts.models import CustomUser 
from rest_framework import serializers

class PlaceSerializer(ModelSerializer):
    userid = serializers.ReadOnlyField(source = 'user.username')
    
    class Meta:
        model = Place
        fields = ['id', 'location', 'pName', 'purpose', 'sTime', 'eTime',
                  'basic_cate', 'detail_cate', 'require', 'link', 'image', 'userid']
        # fields = ['id', 'location', 'pName', 'purpose', 'sTime', 'eTime',
        #           'basic_cate', 'detail_cate', 'require', 'link', 'thumbnail',
        #           'image1', 'image2', 'image3', 'userid']
        
class RestaurantSerializer(ModelSerializer):
    added_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'work_time', 'number','image1', 'image2', 'image3', 'added_by' ]
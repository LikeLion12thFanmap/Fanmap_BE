from rest_framework.routers import SimpleRouter 
from django.urls import path, include
from .views import PlaceViewSet
from .views import RestaurantViewSet

place_router = SimpleRouter(trailing_slash=False)
place_router.register('place', PlaceViewSet, basename='place')

restaurants_router = SimpleRouter(trailing_slash=False)
restaurants_router.register('restaurants', RestaurantViewSet, basename='restaurants')

urlpatterns = [
    path('', include(place_router.urls)),
    path('', include(restaurants_router.urls)),
  ]

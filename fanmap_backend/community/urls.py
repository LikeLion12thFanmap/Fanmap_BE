from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import CommunityViewSet, CommentViewSet

community_router = SimpleRouter(trailing_slash=False)
community_router.register('community', CommunityViewSet, basename='community')

comment_router = SimpleRouter(trailing_slash=False)
comment_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(community_router.urls)),
    path('community/<int:community_id>/', include(comment_router.urls)),
]

from django.urls import path, include
from rest_framework import routers

from .api import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, 'posts')
router.register(r'comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls)),
]
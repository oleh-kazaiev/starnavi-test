from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import serializers
from posts.models import Post
from .services.post_service import PostService


class PostCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PostCreateSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostLikeView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        obj_id = self.kwargs.get('id')
        return PostService().like(post_id=obj_id, user=self.request.user)


class PostDislikeView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        obj_id = self.kwargs.get('id')
        return PostService().dislike(post_id=obj_id, user=self.request.user)

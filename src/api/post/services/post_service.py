from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from posts.models import Post, PostLike, PostDislike


class PostService:
    def like(self, post_id, user):
        post = get_object_or_404(Post, id=post_id)
        dislike = PostDislike.objects.filter(post=post, user=user)
        if dislike.exists():
            dislike.delete()
        like = PostLike.objects.filter(post=post, user=user)
        if like.exists():
            like.delete()
        else:
            PostLike.objects.create(post=post, user=user)
        return Response({'statuss': 'success'})

    def dislike(self, post_id, user):
        post = get_object_or_404(Post, id=post_id)
        like = PostLike.objects.filter(post=post, user=user)
        if like.exists():
            like.delete()
        dislike = PostDislike.objects.filter(post=post, user=user)
        if dislike.exists():
            dislike.delete()
        else:
            PostDislike.objects.create(post=post, user=user)
        return Response({'statuss': 'success'})

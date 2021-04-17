from django.db import models

from accounts.models import User


class Post(models.Model):
    user = models.ForeignKey(to=User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)


class PostLike(models.Model):
    post = models.ForeignKey(to=Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='likes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class PostDislike(models.Model):
    post = models.ForeignKey(to=Post, related_name='dislikes', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='dislikes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

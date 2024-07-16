import datetime
from django.db import models
from django.utils import timezone
from rest_framework import serializers

class Post(models.Model):
    title_text = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title_text
    
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
    

class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    # post = serializers.HyperlinkedRelatedField(view_name='post-detail', queryset=Post.objects.all())  # or use 
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    
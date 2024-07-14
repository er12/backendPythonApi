import datetime
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title_text = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    votes = models.SmallIntegerField(default=0)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.title_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text
    
    
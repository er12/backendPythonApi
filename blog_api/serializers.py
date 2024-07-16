from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'text','post', 'created_at']
        read_only_fields= ('created_at',)
        

class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id','title_text', 'description', 'comments','created_at']
        read_only_fields= ('created_at',)


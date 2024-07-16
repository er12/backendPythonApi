from .models import Post, Comment
from rest_framework import viewsets, permissions 
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer
    
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        
        post_id = request.data.get('post')  # Assuming 'post' is sent in the request data
        post = Post.objects.get(pk=post_id)
        
        # Save the comment with the retrieved Post object
        serializer.save(post=post)
        
        return Response(serializer.data)
    

    
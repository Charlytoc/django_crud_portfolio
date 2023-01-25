from .models import Post, Comments
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer, CommentsSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BlogSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentsSerializer
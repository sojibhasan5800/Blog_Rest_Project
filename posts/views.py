from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions,generics
from .models import Post
from .serializers import PostSerializer
from .permission import IsAuthenticatedReadOnly,IsViewerUser,IsAdminUser

# List all posts or create a new post
class PostListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

# Retrieve, update or delete a single post
class PostdetailView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)

        if post.author != request.user:
            return Response({'detail': 'You do not have permission to edit this post.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)

        if post.author != request.user:
            return Response({'detail': 'You do not have permission to delete this post.'},
                            status=status.HTTP_403_FORBIDDEN)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

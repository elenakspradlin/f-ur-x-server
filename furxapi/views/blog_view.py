"""View module for handling requests for blog data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from furxapi.models import Blog


class BlogView(ViewSet):
    """F UR X API blog view"""

    def list(self, request):
        """Handle GET requests to get all blogs

        Returns:
            Response -- JSON serialized list of blogs
        """

        blogs = Blog.objects.all()
        serialized = BlogSerializer(blogs, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single blog

        Returns:
            Response -- JSON serialized blog record
        """

        blog = Blog.objects.get(pk=pk)
        serialized = BlogSerializer(blog, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class BlogSerializer(serializers.ModelSerializer):
    """JSON serializer for blogs"""
    class Meta:
        model = Blog
        fields = ('id', 'user', 'blog_post',
                  'better_than_yesterday', 'feeling')

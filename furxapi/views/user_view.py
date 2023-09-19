"""View module for handling requests for user data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from furxapi.models import UserProfileInformation
from furxapi.models import Item


class UserView(ViewSet):
    """F UR X API users view"""

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """

        users = UserProfileInformation.objects.all()
        if "current" in request.query_params:
            users = users.filter(user=request.auth.user)
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user record
        """

        user = UserProfileInformation.objects.get(pk=pk)
        serialized = UserSerializer(user, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for registry items"""
    class Meta:
        model = Item
        fields = ('id', 'name', 'picture', 'price', 'url')


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    items = ItemSerializer(many=True)

    class Meta:
        model = UserProfileInformation
        fields = ('id', 'user', 'day_of_breakup', 'items')

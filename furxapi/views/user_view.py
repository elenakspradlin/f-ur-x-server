"""View module for handling requests for user data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from furxapi.models import UserProfileInformation


class UserView(ViewSet):
    """F UR X API users view"""

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """

        users = UserProfileInformation.objects.all()
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


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = UserProfileInformation
        fields = ('id', 'user', 'day_of_breakup')

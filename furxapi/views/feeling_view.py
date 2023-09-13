"""View module for handling requests for feeling data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from furxapi.models import Feeling


class FeelingView(ViewSet):
    """F UR X API feelings view"""

    def list(self, request):
        """Handle GET requests to get all feelings

        Returns:
            Response -- JSON serialized list of feelings
        """

        feelings = Feeling.objects.all()
        serialized = FeelingSerializer(feelings, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single feeling

        Returns:
            Response -- JSON serialized feeling record
        """

        feeling = Feeling.objects.get(pk=pk)
        serialized = FeelingSerializer(feeling, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class FeelingSerializer(serializers.ModelSerializer):
    """JSON serializer for feelings"""
    class Meta:
        model = Feeling
        fields = ('id', 'feeling')

"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from furxapi.models import Item


class ItemView(ViewSet):
    """F UR X API registry items view"""

    def list(self, request):
        """Handle GET requests to get all registry items

        Returns:
            Response -- JSON serialized list of registry items
        """

        items = Item.objects.all()
        serialized = ItemSerializer(items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single registry item

        Returns:
            Response -- JSON serialized registry item record
        """

        item = Item.objects.get(pk=pk)
        serialized = ItemSerializer(item, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for registry items"""
    class Meta:
        model = Item
        fields = ('id', 'picture', 'price', 'url')

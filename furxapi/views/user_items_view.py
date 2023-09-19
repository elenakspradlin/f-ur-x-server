from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from furxapi.models import UserItem, Item, UserProfileInformation


class UserItemView(ViewSet):
    """F UR X API user registry view"""

    def list(self, request):
        """Handle GET requests to get all user's items

        Returns:
            Response -- JSON serialized list of user's items
        """

        user_items = UserItem.objects.all()
        serialized = UserItemSerializer(user_items, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user item

        Returns:
            Response -- JSON serialized user item record
        """

        try:
            user_item = UserItem.objects.get(pk=pk)
            serialized = UserItemSerializer(user_item)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except UserItem.DoesNotExist:
            return Response(
                {'message': 'UserItem not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """Handle POST requests for user items

        Returns:
            Response -- JSON serialized representation of newly created item
        """
        item_id = request.data.get("id")
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return Response(
                {'message': 'Item not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        profile = UserProfileInformation.objects.get(user=request.user)

        new_user_item = UserItem(profile=profile, item=item)
        new_user_item.save()

        serialized = UserItemSerializer(new_user_item)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handles PUT requests for single user item

        Returns:
        Response -- No response body, just 204 status code
        """
        user_item = UserItem.objects.get(pk=pk)

        item_id = request.data.get("id")
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return Response(
                {'message': 'Item not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        user_item.item = item
        user_item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        try:
            user_item = UserItem.objects.get(pk=pk)
            user_item.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except UserItem.DoesNotExist:
            return Response(
                {'message': 'UserItem not found'},
                status=status.HTTP_404_NOT_FOUND
            )


class UserItemSerializer(serializers.ModelSerializer):
    """JSON serializer for user items"""
    class Meta:
        model = UserItem
        fields = ('id', 'item', 'profile')

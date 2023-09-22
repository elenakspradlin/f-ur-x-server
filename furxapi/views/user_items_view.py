from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from furxapi.models import UserItem, Item, UserProfileInformation


class UserItemView(ViewSet):
    """F UR X API user registry view"""

    def list(self, request):
        """Handle GET requests to get all the current user's items
        Returns:
            Returns:
            Response -- JSON serialized list of user's items
        """
        user_items = []

        user_items = UserItem.objects.filter(profile__user=request.auth.user)

        if "current" in request.query_params:

            user_items = user_items.filter(profile=UserItem.profile)

        serialized = UserItemSerializer(user_items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


def retrieve(self, request, pk=None):
    """Handle GET requests for a single user item owned by the current user

    Returns:
    Response -- JSON serialized user item record including associated Item
    """
    try:
        # Retrieve the UserItem instance owned by the current user
        user_item = UserItem.objects.get(
            pk=pk, profile__user=request.auth.user)

        # Serialize UserItem and include the associated Item
        serialized_user_item = UserItemSerializer(user_item)

        # Access the associated Item
        item = user_item.item
        # Assuming you have an ItemSerializer
        serialized_item = ItemSerializer(item)

        # Combine the UserItem and Item data in the response
        response_data = {
            'user_item': serialized_user_item.data,
            'item': serialized_item.data
        }

        return Response(response_data, status=status.HTTP_200_OK)

    except UserItem.DoesNotExist:
        return Response(
            {'message': 'UserItem not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def update(self, request, pk=None):
        """Handles PUT requests for single user item

        Returns:
        Response-- No  response body, just 204 status code"""

        user_item = UserItem.objects.get(pk=pk)
        user_item.name = request.data['name']
        user_item.picture = request.data['picture']
        user_item.price = request.data['price']
        user_item.url = request.data['url']

        # Save the updated item
        user_item.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST requests for creating a user items list

        Returns:
            Response -- JSON serialized user items list
        """
        item = Item.objects.get(pk=request.data["item"])
        profile = UserProfileInformation.objects.get(user=request.auth.user)

        new_user_item = UserItem()

        new_user_item.profile = profile
        new_user_item.item = item
        new_user_item.save()

        serialized = UserItemSerializer(new_user_item, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        try:
            user_item = UserItem.objects.get(pk=pk)
            if user_item.profile.user != request.auth.user:
                return Response(
                    {'message': 'You do not have permission to delete this UserItem'},
                    status=status.HTTP_403_FORBIDDEN
                )

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
        fields = ('id', 'profile', 'item')
        depth = 1

"""View module for handling requests for to do list data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from furxapi.models import ToDoList


class ToDoListView(ViewSet):
    """F UR X API to do list view"""

    def list(self, request):
        """Handle GET requests to get all to do lists

        Returns:
            Response -- JSON serialized list of to do lists
        """

        todo_lists = ToDoList.objects.all()
        serialized = ToDoListSerializer(todo_lists, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single list

        Returns:
            Response -- JSON serialized list record
        """

        todo_list = ToDoList.objects.get(pk=pk)
        serialized = ToDoListSerializer(
            todo_list, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class ToDoListSerializer(serializers.ModelSerializer):
    """JSON serializer for lists"""
    class Meta:
        model = ToDoList
        fields = ('id', 'user', 'to_do_action', 'completed')

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import status, viewsets
from rest_framework.response import Response

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
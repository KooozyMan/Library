from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models.deletion import ProtectedError
from .permissions import IsAdmin

class ProtectedDeleteMixin:

    def perform_destroy(self, instance):

        try:
            instance.delete()

        except ProtectedError:
            raise ValidationError({"detail": ("Cannot delete this record because it is used by books.")})
        

# class BookViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, id=None):
#         queryset = Book.objects.all()
#         book = get_object_or_404(queryset, pk=id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = BookSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.select_related("author","category").all().order_by("id")
    serializer_class = BookSerializer
    permission_classes = [IsAdmin]
    search_fields = ["title"]
    filterset_fields = [
        "author",
        "category",
    ]


class AuthorViewSet(ProtectedDeleteMixin, viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by("id")
    serializer_class = AuthorSerializer
    permission_classes = [IsAdmin]


class CategoryViewSet(ProtectedDeleteMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]
from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'biography', 'birth_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class BookSerializer(serializers.ModelSerializer):
    author_details = AuthorSerializer(source='author', read_only=True)
    category_details = AuthorSerializer(source='category', read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description', 'available_copies', 'published_date', 'author', 'author_details', 'category', 'category_details', 'created_at', 'updated_at']

    def validate_isbn(self, value):
        book = Book.objects.filter(isbn=value)

        if self.instance:
            books = book.exclude(pk=self.instance.pk)

        if books.exists():
            raise serializers.ValidationError('this book already exists')
        
        return value

    def validate_available_copies(self, value):
        if value < 0:
            raise serializers.ValidationError('available copies must not be negative')

        return value
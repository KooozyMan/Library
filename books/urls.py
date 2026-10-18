from .views import BookViewSet
from django.urls import path

urlpatterns = [
    path('api/books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='books'),
    path('api/books/<int:id>', BookViewSet.as_view({'get': 'retrieve'}), name='book'),
]
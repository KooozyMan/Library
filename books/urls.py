from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'books', AuthorViewSet, basename='author')
router.register(r'books', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
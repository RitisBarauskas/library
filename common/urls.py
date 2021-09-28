from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, OneBookOnPageViewSet


router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('books', BookViewSet, basename='books')
router.register('', OneBookOnPageViewSet, basename='book_info')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BookListWithExtra


router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('books', BookViewSet, basename='books')
router.register('', BookListWithExtra, basename='extra_info')

urlpatterns = [
    path('', include(router.urls)),
]

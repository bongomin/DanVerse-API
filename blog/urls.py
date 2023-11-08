from django.urls import path, include
from rest_framework import routers
from .views import BlogPostviewSet, TagsviewSet,CommentviewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blogs', BlogPostviewSet)
router.register(r'tags', TagsviewSet)
router.register(r'comments', CommentviewSet)

urlpatterns = [
    path('', include(router.urls)),
]

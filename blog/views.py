from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TagsSerializer, BlogPostSerializer, CommentSerializer
from .models import Tag,Comment,BlogPost



class TagsviewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class BlogPostviewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class CommentviewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

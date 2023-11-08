from rest_framework import serializers
from .models import Tag,BlogPost,Comment


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tag
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model= BlogPost
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = '__all__'
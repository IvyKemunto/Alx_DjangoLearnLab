from rest_framework import serializers
from .models import Post, Comment, Like
from accounts.serializers import UserListSerializer


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comments."""
    author = UserListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'post', 'author', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts."""
    author = UserListSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'likes_count', 'comments']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']


class PostListSerializer(serializers.ModelSerializer):
    """Serializer for listing posts (without comments)."""
    author = UserListSerializer(read_only=True)
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'likes_count', 'comments_count']

    def get_comments_count(self, obj):
        return obj.comments.count()


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for likes."""
    user = UserListSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

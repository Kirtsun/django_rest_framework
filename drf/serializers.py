from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Comment, Post

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', source="post_set",
                                                queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comm = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', source="comment_set",
                                               queryset=Comment.objects.all(), format='HTML')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'text', 'create', 'author', 'comm']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['url', 'id', 'text', 'create', 'author', 'post']

from rest_framework import serializers

from webapp.models import Photo, Comments, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'text', 'photo', 'author_name', 'created_at')


class PhotoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'description', 'image', 'creation_date', 'likes', 'author_name', 'comments')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'photo', 'like')

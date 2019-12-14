from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from webapp.models import Photo, Comments, Like

from api_v1.serializers import PhotoSerializer, CommentSerializer, LikeSerializer


from django.core.serializers import serialize, deserialize
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@action(methods=['post'], detail=True)
def rate_up(self, request, pk=None):
    like = self.get_object()
    like.like += 1
    like.save()
    return Response({'id': like.pk, 'rating': like.rating})


class PhotoViewSet(viewsets.ModelViewSet):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @action(methods=['post'], detail=True)
    def like_up(self, request, pk=None):
        photo = self.get_object()
        photo.likes += 1
        photo.save()
        return Response({'id': photo.pk, 'rating': photo.likes})

    @action(methods=['post'], detail=True)
    def like_down(self, request, pk=None):
        photo = self.get_object()
        photo.likes -= 1
        photo.save()
        return Response({'id': photo.pk, 'rating': photo.likes})

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()


# class LikeViewSet(viewsets.ModelViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.none()
    serializer_class = LikeSerializer

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Like.objects.all()
    #     return Quote.objects.filter(status=QUOTE_APPROVED)

    # def get_permissions(self):
    #     if self.action not in ['update', 'partial_update', 'destroy']:
    #         return [AllowAny()]
    #     return [IsAuthenticated()]


@action(methods=['post'], detail=True)
def rate_down(self, request, pk=None):
    like = self.get_object()
    like.like -= 1
    like.save()
    return Response({'id': like.pk, 'rating': like.rating})

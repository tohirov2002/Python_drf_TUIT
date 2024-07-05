from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Comments
from .serializers import CommentsSerializers
from app_journal.permissions import IsAdminReadOnly
from .filters import CommentsFilterArticles


class CommentsView(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CommentsFilterArticles
    # permission_classes = [IsAdminReadOnly]
    http_method_names = ["get", "post", "delete"]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Comments.objects.filter(comment_status=True))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializers = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializers.data)

        serializers = self.get_serializer(queryset, many=True)
        return Response(serializers.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == self.request.user:
            instance.comment_status = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def set_reaction(request, comment_id, reaction_type):
    if request.user.is_authenticated:
        try:
            comment = Comments.objects.get(pk=comment_id)
            if reaction_type == "like":
                if request.user in comment.comment_likes.all():
                    comment.comment_likes.remove(request.user)
                    return Response(
                        data={"message": "Like canceled"}, status=status.HTTP_200_OK
                    )
                else:
                    comment.comment_likes.add(request.user)
                    if request.user in comment.comment_dislikes.all():
                        comment.comment_dislikes.remove(request.user)
                    return Response(
                        data={"message": "Liked"}, status=status.HTTP_200_OK
                    )
            elif reaction_type == "dislike":
                if request.user in comment.comment_dislikes.all():
                    comment.comment_dislikes.remove(request.user)
                    return Response(
                        data={"message": "DisLike canceled"}, status=status.HTTP_200_OK
                    )
                else:
                    comment.comment_dislikes.add(request.user)
                    if request.user in comment.comment_likes.all():
                        comment.comment_likes.remove(request.user)
                    return Response(
                        data={"message": "DisLiked"}, status=status.HTTP_200_OK
                    )
            else:
                return Response(
                    data={"message": "invalid reaction type"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Comments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

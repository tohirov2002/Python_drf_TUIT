from rest_framework import viewsets
from time import time
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response

from .models import Category, ArticlesModel
from .serializers import (
    CategorySerializers,
    ArticlesSerializers,
    ArticlesGetSerializers,
    ArticlesGetSerializer,
)
from .filters import ArticlesFilter
from app_journal.permissions import IsAdminReadOnly


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminReadOnly]


class ArticlesView(viewsets.ModelViewSet):
    queryset = ArticlesModel.objects.all()
    # permission_classes = [IsAdminReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ArticlesFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            return Response(
                {"error": "Only authenticated users can create articles."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return serializer.save()

    def get_serializer_class(self):
        if self.request.method == "GET" and "pk" not in self.kwargs:
            return ArticlesGetSerializers
        return ArticlesSerializers

    def retrieve(self, request, pk=None, *args, **kwargs):
        title = f"article_{pk}"
        if title in request.COOKIES:
            if time() - float(request.COOKIES[title]) > 10:
                up = True
            else:
                up = False
        else:
            up = True
        if up:
            doc = ArticlesModel.objects.get(pk=pk).eye
            ArticlesModel.objects.filter(pk=pk).update(eye=doc + 1)
        response = super().retrieve(request, pk, *args, **kwargs)
        response.set_cookie(title, time())
        return response

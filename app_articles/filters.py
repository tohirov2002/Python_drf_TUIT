import django_filters
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import ArticlesModel, Category


class ArticlesFilter(django_filters.FilterSet):
    title_uz = django_filters.CharFilter(lookup_expr='icontains', field_name='title_uz')
    author = django_filters.ModelChoiceFilter(queryset=get_user_model().objects.all(), field_name='author')
    keywords = django_filters.CharFilter(lookup_expr='icontains', field_name='keywords')
    references = django_filters.CharFilter(lookup_expr='icontains', field_name='references')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), field_name='category')

    class Meta:
        model = ArticlesModel
        fields = []





import django_filters

from .models import Comments


class CommentsFilterArticles(django_filters.FilterSet):
    comment_doc = django_filters.CharFilter(lookup_expr='exact', field_name='comment_doc')

    class Meta:
        model = Comments
        fields = {'comment_doc': ['exact']}

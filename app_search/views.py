from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from app_articles.models import ArticlesModel
from app_journal.models import JournalModel


@api_view(['GET'])
def all_search(request):
    keyword = request.GET.get('keyword', None)
    if keyword:
        articles = ArticlesModel.objects.filter(title_uz__icontains=keyword).values_list('id')
        journal = JournalModel.objects.filter(description_uz__icontains=keyword).values_list('id')
        response = Response(status=status.HTTP_200_OK)
        result = list(articles) + list(journal)

        a = [0] * len(result)

        for i in range(len(result)):
            a[i] = (result[i][0])

        res = ArticlesModel.objects.filter(id__in=set(a)).values()
        response.data = {
            'docs': list(res)
        }
        return response
    return Response(
        data={'message': 'Insert keyword please!'},
        status=status.HTTP_400_BAD_REQUEST
    )


# @api_view(['GET'])
# def search(request):
#     keyword = request.GET.get('keyword')
#     if keyword:
#         articles = list(
#             ArticleModel.objects.filter(
#                 (Q(article_title_uz__icontains=keyword) | Q(article_title_en__icontains=keyword) |
#                 Q(article_description_uz__icontains=keyword) | Q(article_description_en__icontains=keyword) |
#                 Q(article_text_uz__icontains=keyword) | Q(article_text_en__icontains=keyword) |
#                 Q(keywords__icontains=keyword) | Q(references__icontains=keyword)) and Q(status=True)
#             )
#         )
#         journals = list(
#             JournalModel.objects.filter(
#                 (Q(journal_description_uz__icontains=keyword) | Q(journal_description_en__icontains=keyword)) and
#                 Q(journal_status=True)
#             )
#         )
#
#         articles_data = ArticleSerializer(articles, many=True).data
#         journals_data = JournalSerializer(journals, many=True).data
#
#         res = Response(status=status.HTTP_200_OK)
#         res.data = {
#             'journal': journals_data,
#             'article': articles_data
#         }
#         return res
#     return Response(
#         data={'message': 'Enter keyword'},
#         status=status.HTTP_400_BAD_REQUEST
#     )

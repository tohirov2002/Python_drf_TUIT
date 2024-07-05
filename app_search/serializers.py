from rest_framework import serializers

from app_articles.serializers import ArticlesSerializers
from app_journal.serializers import JournalSerializers


class SearchAllSerializers(serializers.Serializer):
    articles = ArticlesSerializers
    journal = JournalSerializers

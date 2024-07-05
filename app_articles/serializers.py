from rest_framework import serializers

from .models import Category, ArticlesModel
from app_journal.serializers import JournalSerializers


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ArticlesSerializers(serializers.ModelSerializer):

    class Meta:
        model = ArticlesModel
        fields = "__all__"
        extra_kwargs = {"author": {"read_only": True}}


class ArticlesGetSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(method_name="get_name", read_only=True)
    annotation = serializers.SerializerMethodField(
        method_name="get_names", read_only=True
    )

    class Meta:
        model = ArticlesModel
        fields = (
            "id",
            "title",
            "annotation",
        )

    def get_name(self, obj):
        try:
            lang = self.context["request"].GET["lang"]
            if lang == "ru":
                return obj.title_ru
            return obj.title_uz
        except:
            return obj.title_uz

    def get_names(self, obj):
        try:
            lang = self.context["request"].GET["lang"]
            if lang == "ru":
                return obj.annotation_ru
            return obj.annotation_uz
        except:
            return obj.annotation_uz


class ArticlesGetSerializers(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(method_name="get_name", read_only=True)
    annotation = serializers.SerializerMethodField(
        method_name="get_names", read_only=True
    )
    date_time = serializers.SerializerMethodField(
        method_name="get_times", read_only=True
    )
    eye = serializers.SerializerMethodField(method_name="get_eye", read_only=True)
    author = serializers.SerializerMethodField(method_name="get_author", read_only=True)

    class Meta:
        model = ArticlesModel
        fields = ("id", "title", "annotation", "date_time", "eye", "author", "category")

    def get_name(self, obj):
        try:
            lang = self.context["request"].GET["lang"]
            if lang == "ru":
                return obj.title_ru
            return obj.title_uz
        except:
            return obj.title_uz

    def get_names(self, obj):
        try:
            lang = self.context["request"].GET["lang"]
            if lang == "ru":
                return obj.annotation_ru
            return obj.annotation_uz
        except:
            return obj.annotation_uz

    def get_eye(self, obj):
        return obj.eye

    def get_times(self, obj):
        return obj.date_time

    def get_author(self, obj):
        return obj.author.id

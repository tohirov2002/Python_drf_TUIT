from rest_framework import serializers

from .models import JournalModel
from app_articles.models import Category


class JournalSerializers(serializers.ModelSerializer):

    class Meta:
        model = JournalModel
        fields = "__all__"


class JournalGetSerializers(serializers.ModelSerializer):
    description = serializers.SerializerMethodField(
        method_name="get_name", read_only=True
    )

    class Meta:
        model = JournalModel
        fields = (
            "id",
            "description",
            "logo",
        )

    def get_name(self, obj):
        try:
            lang = self.context["request"].GET["lang"]
            if lang == "ru":
                return obj.description_ru
            return obj.description_uz
        except:
            return obj.description_uz

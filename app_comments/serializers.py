from rest_framework import serializers

from .models import Comments


class CommentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"
        extra_kwargs = {
            "author": {"read_only": True},
            "comment_likes": {"read_only": True},
            "comment_dislikes": {"read_only": True},
        }

from rest_framework import serializers

from .models import Requirements


class RequirementsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = "__all__"

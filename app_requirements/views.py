from rest_framework import viewsets

from .models import Requirements
from .serializers import RequirementsSerializers
from app_journal.permissions import IsAdminReadOnly


class RequirementsView(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializers
    # permission_classes = [IsAdminReadOnly]yt

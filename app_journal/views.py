from rest_framework import viewsets

from .models import JournalModel
from .serializers import JournalSerializers, JournalGetSerializers
from .permissions import IsAdminReadOnly


class JournalView(viewsets.ModelViewSet):
    queryset = JournalModel.objects.all()
    # permission_classes = [IsAdminReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET" and "pk" not in self.kwargs:
            return JournalGetSerializers
        return JournalSerializers

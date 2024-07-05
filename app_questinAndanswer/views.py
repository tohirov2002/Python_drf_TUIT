from rest_framework import viewsets

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from app_journal.permissions import IsAdminReadOnly


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAdminReadOnly]


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    # permission_classes = [IsAdminReadOnly]

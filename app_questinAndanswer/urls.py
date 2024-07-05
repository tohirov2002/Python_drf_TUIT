from rest_framework.routers import DefaultRouter

from .views import QuestionView, AnswerView

router = DefaultRouter()

router.register(r"question", QuestionView)
router.register(r"answer", AnswerView)

urlpatterns = router.urls

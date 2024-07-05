from rest_framework.routers import DefaultRouter

from .views import JournalView

router = DefaultRouter()

router.register(r"", JournalView)

urlpatterns = router.urls

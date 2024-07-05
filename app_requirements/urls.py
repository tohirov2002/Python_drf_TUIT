from rest_framework.routers import DefaultRouter

from .views import RequirementsView

router = DefaultRouter()

router.register(r"", RequirementsView)

urlpatterns = router.urls

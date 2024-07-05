from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CategoryView, ArticlesView

router = DefaultRouter()

router.register(r"category", CategoryView)
router.register(r"", ArticlesView, basename="articles")

urlpatterns = router.urls

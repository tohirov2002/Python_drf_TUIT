from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CommentsView, set_reaction

router = DefaultRouter()

router.register(r"", CommentsView)

urlpatterns = router.urls

urlpatterns += [
    path(
        "reaction/<int:comment_id>/<str:reaction_type>/",
        set_reaction,
        name="set_reaction",
    )
]

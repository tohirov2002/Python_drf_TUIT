from rest_framework.routers import DefaultRouter

from .views import SendContactsView

router = DefaultRouter()

router.register(r"emailsend", SendContactsView)

urlpatterns = router.urls

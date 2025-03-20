from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from markflow.documents.api.views import DocumentViewSet
from markflow.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("documents", DocumentViewSet)



app_name = "api"
urlpatterns = router.urls

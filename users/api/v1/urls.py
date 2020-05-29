from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SefrtgViewSet

router = DefaultRouter()
router.register("sefrtg", SefrtgViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

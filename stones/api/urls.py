from django.urls import include, path
from rest_framework import routers

from api.views import (
    HeaderViewSet,
    ServiceViewSet,
    MaterialViewSet,
    NavigationViewSet,
    ContactViewSet,
    FooterViewSet,
)

app = "api"

router = routers.DefaultRouter()
router.register(
    r"header",
    HeaderViewSet,
)
router.register(
    r"services",
    ServiceViewSet,
)
router.register(
    r"materials",
    MaterialViewSet,
)
router.register(
    r"navigation",
    NavigationViewSet,
)
router.register(
    r"contact",
    ContactViewSet,
)
router.register(
    r"footer",
    FooterViewSet,
)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

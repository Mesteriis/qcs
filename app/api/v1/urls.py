from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter

from .files import CodeFilesViewSet
from .report import ReportViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("files", CodeFilesViewSet)
router.register("report", ReportViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/schema/", SpectacularAPIView.as_view(), name="api-schema_v1"),
    path("v1/token/", obtain_auth_token),
    path(
        "v1/docs/",
        SpectacularSwaggerView.as_view(url_name="api:api-schema_v1"),
        name="api-docs_v1",
    ),
]

from django.db.models import QuerySet
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import ReportSerializer, Report


class ReportViewSet(
    ListModelMixin,
    GenericViewSet,
):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

    def get_queryset(self) -> QuerySet[Report]:
        return self.queryset.filter(user=self.request.user)

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from reports.service import CQService
from .serializers import CodeFilesSerializer, CodeFile
from ..report import ReportSerializer


class CodeFilesViewSet(
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet,
    CreateModelMixin,
):
    serializer_class = CodeFilesSerializer
    queryset = CodeFile.objects.all().order_by("-created")

    def get_queryset(self) -> QuerySet[CodeFile]:
        return self.queryset.filter(user=self.request.user)

    @action(methods=["POST"], detail=True)
    def processing(self, request, pk=None) -> Response:
        file_ = self.get_object()
        result = CQService.check_from_model(file_)
        return Response(ReportSerializer(result).data, status=status.HTTP_200_OK)

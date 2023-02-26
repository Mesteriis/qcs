from django.contrib.auth import get_user_model
from django.db import models

from .constants import ReportStatus


class Report(models.Model):
    file = models.OneToOneField('files.CodeFile', null=False, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(
        get_user_model(),
        verbose_name="user",
        on_delete=models.DO_NOTHING,
        null=False
    )
    result = models.JSONField(null=True, blank=True)
    status = models.CharField(choices=ReportStatus, default=ReportStatus.SUCCESS, max_length=1)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    is_sent = models.BooleanField(default=False)

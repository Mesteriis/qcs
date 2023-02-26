import contextlib
from datetime import datetime
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models


def file_handler(instance, filename):
    return f"code_files/user_{instance.user.id}/{datetime.now().timestamp()}/{filename}"


class CodeFile(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(
        get_user_model(),
        verbose_name="user",
        on_delete=models.CASCADE,
        null=False,
    )

    file = models.FileField(
        upload_to=file_handler,
        validators=[
            FileExtensionValidator(allowed_extensions=["py"]),
        ],
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    @property
    def status(self):
        with contextlib.suppress(Exception):
            return self.report.status
        return "new"

from logging import getLogger

from config import celery_app
from files.models import CodeFile
from reports.service import CQService

logger = getLogger("checker")


@celery_app.task()
def check_files():
    for file in CodeFile.objects.filter(report__isnull=True):
        report = CQService.check_from_model(file)
        logger.info(
            "Проверили файл {report}, result: {status}",
            extra={
                "report": report.file.pk,
                "status": report.status,
            },
        )

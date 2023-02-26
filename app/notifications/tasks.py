from logging import getLogger

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from config import celery_app
from reports.models import Report

logger = getLogger("notification")


@celery_app.task()
def sent_mail_notify():
    for report in Report.objects.filter(is_sent=False):
        subject = f"report on the file: {report.file.file.name.split('/')[-1]}"
        html_message = render_to_string("pages/report.html", {"report": report})
        plain_message = strip_tags(html_message)
        to = report.user.email
        mail.send_mail(
            subject=subject,
            message=plain_message,
            from_email=None,
            recipient_list=[to],
            html_message=html_message,
        )
        report.is_sent = True
        report.save()
        logger.info("Sent mail {to}", extra={"to": to})

import os
import sys
from pathlib import Path
from celery import Celery

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

app = Celery("app")
sys.path.append(str(ROOT_DIR / "app"))
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

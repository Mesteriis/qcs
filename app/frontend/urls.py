from django.urls import path

from frontend.views import home, report

app_name = "frontend"
urlpatterns = [
    path("", home, name="home"),
    path("report/<uuid:file_uid>", report, name="report"),
]

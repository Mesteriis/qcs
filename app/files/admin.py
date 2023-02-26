from django.contrib import admin

from files.models import CodeFile
from reports.models import Report


class ReportsInLine(admin.TabularInline):
    model = Report
    extra = 0
    fields = [
        "result",
    ]

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CodeFile)
class CodeFilesAdmin(admin.ModelAdmin):
    inlines = [ReportsInLine]

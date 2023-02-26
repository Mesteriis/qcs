from django.utils.translation import gettext_lazy as _
from django_better_choices import Choices


class ReportStatus(Choices):
    SUCCESS = Choices.Value(_("Success"), help_text=_("Success"), value="s")
    FAIL = Choices.Value(_("Fail"), help_text=_("Fail"), value="f")

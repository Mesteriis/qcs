from django.utils.translation import gettext_lazy as _
from django_better_choices import Choices


class FileStatus(Choices):
    NEW = Choices.Value(_("New"), help_text=_("New file"), value="n")
    VALID = Choices.Value(_("Valid"), help_text=_("Valid file"), value="v")
    INVALID = Choices.Value(_("Invalid"), help_text=_("invalid file"), value="i")

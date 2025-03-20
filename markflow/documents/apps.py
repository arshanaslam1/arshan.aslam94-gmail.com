import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DocumentsConfig(AppConfig):
    name = "markflow.documents"
    verbose_name = _("Documents")

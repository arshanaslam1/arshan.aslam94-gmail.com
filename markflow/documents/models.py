
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, TextField, ForeignKey, ManyToManyField
from django.db.models import EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from markflow.users.models import User


class Document(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=255)
    content = models.TextField(_("Content"))
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    tags =models.ManyToManyField('Tag', verbose_name=_("Tags"), related_name="tags")

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")


class Tag(TimeStampedModel):
    name= CharField(_("Name"), max_length=255)
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

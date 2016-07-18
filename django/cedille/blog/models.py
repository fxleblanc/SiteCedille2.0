from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):

    class Meta:
        verbose_name_plural = _('members')

    text = models.TextField(
        verbose_name=_('Notes')
    )

    author = models.ForeignKey(
        User,
        verbose_name=_('Author'),
        related_name='Notes'
        )

    date = models.DateField(
        verbose_name=_('Date'),
        default=timezone.now,
    )

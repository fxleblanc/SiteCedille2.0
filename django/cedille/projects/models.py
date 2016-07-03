from django.db import models
from django.utils.translation import ugettext_lazy as _

PROJECT_STATUS = (
    ('A', _('Active')),
    ('D', _('Done')),

)


class Project(models.Model):

    class Meta:
        verbose_name_plural = _('projects')

    name = models.CharField(
        max_length=100,
        verbose_name=_('name')
    )

    description = models.TextField(
        verbose_name=_('description')
    )

    github = models.CharField(
        max_length=100,
        verbose_name=_('github')
    )

    status = models.CharField(
        max_length=1,
        verbose_name=_('status')
    )

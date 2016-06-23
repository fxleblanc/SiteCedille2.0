from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Partner(models.Model):

    class Meta:
        verbose_name_plural = _('partners')

    partnername = models.CharField(
        max_length=100,
        verbose_name=_('partnername')
    )

    logo = models.ImageField(
        verbose_name=_('logo')
    )

    website = models.CharField(
        max_length=300,
        verbose_name=_('website')
    )

    status = models.BooleanField(
        verbose_name=_('status')
    )

    ranking = models.CharField(
        verbose_name=_('ranking')
    )

    def __str__(self):
        return "{}".format(self.partnername)

from django.db import models
from django.utils.translation import ugettext_lazy as _

MEMBER_STATUS = (
    ('A', _('Active')),
    ('I', _('Inactif')),
    ('E', _('Ex-Member')),
)


class Member(models.Model):

    class Meta:
        verbose_name_plural = _('members')

    firstname = models.CharField(
        max_length=50,
        verbose_name=_('firstname')
    )

    lastname = models.CharField(
        max_length=50,
        verbose_name=_('lastname')
    )

    status = models.CharField(
        max_length=1,
        choices=MEMBER_STATUS,
    )

    biography = models.TextField(
        verbose_name=_('Biography')
    )

    title = models.TextField(
        verbose_name=_('Title')
    )

    picture = models.ImageField(
            verbose_name=_('picture'),
            blank=True,
            null=True,
            upload_to='avatars/'
        )

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    date = models.DateField(_('date'), unique=True)
    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __str__(self):
        return 'Modelbouwdag {}'.format(self.date)

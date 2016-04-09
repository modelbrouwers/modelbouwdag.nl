from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField


class Event(models.Model):
    date = models.DateField(_('date'), unique=True)
    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2, null=True, blank=True)

    sponsors = models.ManyToManyField('Sponsor', through='EventSponsor', related_name='events', blank=True)

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __str__(self):
        return 'Modelbouwdag {}'.format(self.date)


class Sponsor(models.Model):
    name = models.CharField(_('name'), max_length=50)
    logo = FilerImageField(verbose_name=_('logo'))
    url = models.URLField(_('url'))

    class Meta:
        verbose_name = _('sponsor')
        verbose_name_plural = _('sponsors')

    def __str__(self):
        return self.name


class EventSponsor(models.Model):
    event = models.ForeignKey(Event)
    sponsor = models.ForeignKey(Sponsor)
    order = models.PositiveIntegerField(default=0)


class SponsorListPlugin(CMSPlugin):
    for_event = models.ForeignKey(Event, verbose_name=_('event'))

    class Meta:
        verbose_name = _('sponsor list')
        verbose_name_plural = _('sponsor lists')

    def __str__(self):
        return _('{n} sponsors for modelbouwdag {year}').format(
            year=self.for_event.date.year,
            n=EventSponsor.objects.filter(event=self.for_event).count()
        )

from datetime import date

from django.db import models
from django.utils.text import mark_safe
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
import markdown

from modelbouwdag.events.models import Event


def get_upcoming_event():
    events = Event.objects.filter(date__gte=date.today())
    return events.order_by('date').first()


def get_next_order():
    result = Exhibitor.objects.aggregate(max=models.Max('order'))
    return result.get('max', 0) + 1


class ExhibitorType(models.Model):
    name = models.CharField(_('name'), max_length=100)
    code = models.CharField(_('code'), max_length=10, unique=True)

    def __str__(self):
        return self.name


class Exhibitor(models.Model):
    event = models.ForeignKey(Event, default=get_upcoming_event)
    name = models.CharField(
        _('name'), max_length=255,
        help_text=_('To embed links, use the following syntax: [text-for-the-link]({url}). '
                    'You can enter an actual url, or leave the {url} placeholder, which will '
                    'be replaced by the exhibitors url.')
    )
    types = models.ManyToManyField(ExhibitorType, verbose_name=_('types'), blank=True)
    url = models.URLField(_('url'), blank=True)
    description = models.CharField(
        _('description'), max_length=500, blank=True,
        help_text=_('To embed links, use the following syntax: [text-for-the-link]({url}). '
                    'You can enter an actual url, or leave the {url} placeholder, which will '
                    'be replaced by the exhibitors url.')
    )
    order = models.PositiveIntegerField(_('order'), default=get_next_order)

    def __str__(self):
        return self.name

    def get_name(self):
        name = self.name.format(url=self.url) if self.url else self.name
        return mark_safe(markdown.markdown(name))

    def get_description(self):
        if not self.description:
            return ''
        desc = self.description.format(url=self.url) if self.url else self.description
        return mark_safe(markdown.markdown(desc))


class ExhibitorListPlugin(CMSPlugin):
    for_event = models.ForeignKey(Event)

    class Meta:
        verbose_name = _('exhibitor list')
        verbose_name_plural = _('exhibitor lists')

    def __str__(self):
        return _('{n} exhibitors for modelbouwdag {year}').format(
            year=self.for_event.date.year,
            n=Exhibitor.objects.filter(event=self.for_event).count()
        )

    @property
    def exhibitors(self):
        return self.for_event.exhibitor_set.prefetch_related('types').order_by('order', 'name')

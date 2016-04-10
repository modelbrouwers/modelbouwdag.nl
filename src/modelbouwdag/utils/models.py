from django.core.exceptions import ValidationError
from django.db import models

from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField


class Divider(CMSPlugin):

    label = models.CharField(_('label'), max_length=50)

    class Meta:
        verbose_name = _('divider')
        verbose_name_plural = _('dividers')

    def __str__(self):
        return _('{label} - divider {pk}').format(label=self.label, pk=self.pk)

    @property
    def html_id(self):
        return 'divider_%d' % self.pk


class MenuItem(CMSPlugin):
    """
    In-page menu item.
    """
    title = models.CharField(_('title'), max_length=100)
    url = models.URLField(_('url'), blank=True, help_text=_('has precedence over href'))
    href = models.CharField(_('href'), max_length=255, blank=True)
    image = FilerImageField(blank=True, null=True)

    class Meta:
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')

    def __str__(self):
        return self.title

    def clean(self):
        if not self.url and not self.href:
            raise ValidationError(_('Either url or href must be supplied'))

    def get_href(self):
        return self.url or self.href

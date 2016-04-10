from django.db import models

from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


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

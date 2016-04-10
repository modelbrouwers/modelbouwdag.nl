from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class Divider(CMSPlugin):
    pass

    class Meta:
        verbose_name = _('divider')
        verbose_name_plural = _('dividers')

    def __str__(self):
        return _('divider %d') % self.pk

    @property
    def html_id(self):
        return 'divider_%d' % self.pk

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.utils.translation import ugettext_lazy as _

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
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


class FacebookPage(CMSPlugin):
    """
    Facebook page plugin (widget)
    """
    facebook_page_url = models.URLField(_('facebook page url'))
    tabs = models.CharField(_('tabs'), max_length=255, default='timeline')
    width = models.PositiveSmallIntegerField(
        _('width'), blank=True, null=True,
        validators=[MinValueValidator(180), MaxValueValidator(500)]
    )
    height = models.PositiveSmallIntegerField(
        _('height'), blank=True, null=True,
        validators=[MinValueValidator(70)]
    )
    small_header = models.BooleanField(_('use small header'), default=False)
    hide_cover_photo = models.BooleanField(_('hide cover photo'), default=False)
    adapt_to_container_width = models.BooleanField(_('adapt to container width'), default=True)
    show_friends_faces = models.BooleanField(_('show friend\'s faces'), default=True)

    class Meta:
        verbose_name = _('facebook page plugin')
        verbose_name_plural = _('facebook page plugins')

    def __str__(self):
        return self.facebook_page_url


class IconExtension(PageExtension):
    image = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL)


extension_pool.register(IconExtension)

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import models


class DividerPlugin(CMSPluginBase):
    model = models.Divider
    render_template = "plugins/divider.html"
    name = _('divider')


plugin_pool.register_plugin(DividerPlugin)
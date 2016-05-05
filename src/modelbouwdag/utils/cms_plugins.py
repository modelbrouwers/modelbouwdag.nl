from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import models


@plugin_pool.register_plugin
class DividerPlugin(CMSPluginBase):
    model = models.Divider
    render_template = "plugins/divider.html"
    name = _('divider')


@plugin_pool.register_plugin
class MenuItemPlugin(CMSPluginBase):
    model = models.MenuItem
    render_template = "plugins/menu_item.html"
    name = _('menu item')


@plugin_pool.register_plugin
class FacebookPagePlugin(CMSPluginBase):
    model = models.FacebookPage
    render_template = "plugins/facebook_page.html"
    name = _('facebook page plugin')

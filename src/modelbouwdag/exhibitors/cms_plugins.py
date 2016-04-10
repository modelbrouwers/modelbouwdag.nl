from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import models


class ExhibitorListPlugin(CMSPluginBase):
    module = 'Exhibitors'
    model = models.ExhibitorListPlugin
    name = _('exhibitor list')
    render_template = "exhibitors/plugins/list.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['exhibitors'] = instance.for_event.exhibitor_set.prefetch_related('types').order_by('order', 'name')
        return context


plugin_pool.register_plugin(ExhibitorListPlugin)

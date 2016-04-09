from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import models


class SponsorListPlugin(CMSPluginBase):
    module = 'Events'
    model = models.SponsorListPlugin
    render_template = "events/plugins/sponsor_list.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        event_sponsors = instance.for_event.eventsponsor_set.select_related('sponsor')
        context['event_sponsors'] = event_sponsors.order_by('order', 'sponsor__pk')
        return context


plugin_pool.register_plugin(SponsorListPlugin)

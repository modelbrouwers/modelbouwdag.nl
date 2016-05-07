from django.core.exceptions import ObjectDoesNotExist

from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Page


@menu_pool.register_modifier
class IconModifier(Modifier):
    """
    Adds the page icon to the menu if it exists
    """

    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        # if the menu is not yet cut, don't do anything
        if post_cut:
            return nodes
        # otherwise loop over the nodes
        for node in nodes:
            # does this node represent a Page?
            if node.attr["is_page"]:
                page = Page.objects.get(id=node.id)
                try:
                    extension = page.iconextension
                    node.attr['icon'] = extension.image
                except ObjectDoesNotExist:
                    pass
        return nodes

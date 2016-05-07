from django.contrib import admin

from cms.extensions import PageExtensionAdmin

from .models import IconExtension


@admin.register(IconExtension)
class IconExtensionAdmin(PageExtensionAdmin):
    pass

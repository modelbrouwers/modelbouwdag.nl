from django.contrib import admin

from .models import Exhibitor, ExhibitorType


@admin.register(Exhibitor)
class ExhibitorAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'get_name', 'get_description', 'order']
    list_editable = ['order']
    list_filter = ['event']
    search_fields = ['name', 'description']
    filter_horizontal = ['types']
    ordering = ['order']


@admin.register(ExhibitorType)
class ExhibitorTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']

from django.contrib import admin

from .models import Event, EventSponsor, Sponsor


class EventSponsorInline(admin.TabularInline):
    model = EventSponsor
    raw_id_fields = ['sponsor']
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'price')
    ordering = ('-date',)
    inlines = [EventSponsorInline]


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    search_fields = ['name']

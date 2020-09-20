from django.contrib import admin

from .models import Traffic, Source, Country, PIR, event_type, Organizations, Equipment, EventMatrix

#admin.site.register(Traffic)
admin.site.register(Source)
admin.site.register(Country)
admin.site.register(PIR)
admin.site.register(event_type)
admin.site.register(Organizations)
admin.site.register(Equipment)

#@admin.register(Source)
#class SourceAdmin(admin.ModelAdmin):
#	list_display = ['source_name']


@admin.register(Traffic)
class TrafficAdmin(admin.ModelAdmin):
	list_display = ('docname', 'traffic_slug','docdate', 'source','PIR','grids', 'status')
	list_filter = ('status','docdate', 'source')
	search_fields = ('docname', 'fulltext')
	prepopulated_fields = {'traffic_slug': ('docname',)}
	date_hierarchy = 'docdate'
	ordering = ('status','docdate')

@admin.register(EventMatrix)
class EventAdmin(admin.ModelAdmin):
	list_display = ('reference', 'event', 'location')
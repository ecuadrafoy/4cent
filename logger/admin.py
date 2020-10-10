from django.contrib import admin

from .models import Traffic, Source, Country, PIR, event_type, Organizations, Equipment, EventMatrix, Notes

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

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title','created_on','user','active')
    list_filter = ('active','created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.forms import CheckboxSelectMultiple
import csv, datetime

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

User = get_user_model()

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' 'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response

export_to_csv.short_description = 'Export to CSV'  #short description


@admin.register(Traffic)
class TrafficAdmin(admin.ModelAdmin):
	list_display = ('docname', 'traffic_slug','docdate', 'source','grids', 'status')
	list_filter = ('status','docdate', 'source')
	search_fields = ('docname', 'fulltext')
	prepopulated_fields = {'traffic_slug': ('docname',)}
	date_hierarchy = 'docdate'
	ordering = ('status','docdate')
	actions = [export_to_csv]

@admin.register(EventMatrix)
class EventAdmin(admin.ModelAdmin):
	list_display = ('reference', 'event', 'location')
	actions = [export_to_csv]

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title','created_on','user','active')
    list_filter = ('active','created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
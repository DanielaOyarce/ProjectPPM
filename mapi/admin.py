from django.contrib import admin
from .models import Mapi

class MapiAdmin(admin.ModelAdmin):
	list_display = ('aircraft', 'ata', 'subata', 'week', 'nmfl', 'dtlmfl', 'flight_number', 'sta', 'reference_term', 'nri', 'dmi', 'cat', 'duedate', 'discrepancies', 'action_correct', 'part_number', 'position', 'status', 'found_on_date')
	list_filter = ('found_on_date', 'aircraft__name',)
	ordering = ('found_on_date',)
	search_fields = ('aircraft__name',)

admin.site.register(Mapi, MapiAdmin)


	
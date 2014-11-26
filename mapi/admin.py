from django.contrib import admin
from .models import Mapi

class MapiAdmin(admin.ModelAdmin):
	list_display = ('referenceTerm', 'foundOnDate', 'flightNumber', 'aircraft', 'ata', 'subAta', 'sta', 'nri', 'discrepancies', 'actionCorrect', 'status',)
	list_filter = ('foundOnDate',)
	ordering = ('foundOnDate',)
	search_fields = ('aircraft__name',)

admin.site.register(Mapi, MapiAdmin)

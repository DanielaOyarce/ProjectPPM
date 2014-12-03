from django.contrib import admin
from .models import Mapi, Aircraft

class MapiAdmin(admin.ModelAdmin):
	list_display = ('referenceTerm', 'foundOnDate', 'flightNumber', 'aircraft', 'ata', 'subAta', 'sta', 'nri', 'discrepancies', 'actionCorrect', 'status',)
	list_filter = ('foundOnDate', 'aircraft__name',)
	ordering = ('foundOnDate',)
	search_fields = ('aircraft__name',)

admin.site.register(Mapi, MapiAdmin)

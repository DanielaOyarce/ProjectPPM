from django.contrib import admin
from .models import Mapi

#class MapiAdmin(admin.ModelAdmin):
#	list_display = ('aircraft', 'ata', 'subAta', 'week', 'nmfl', 'dtlmfl', 'flightNumber', 'sta', 'referenceTerm', 'nri', 'dmi', 'cat', 'dueDate', 'discrepancies', 'actionCorrect', 'partNumber', 'position', 'status', 'foundOnDate')

admin.site.register(Mapi)

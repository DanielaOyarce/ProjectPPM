from django.contrib import admin
from .models import Aircraft, Operator, Fleet, Manufacturer

class AircraftAdmin(admin.ModelAdmin):
	list_display = ('name', 'status')	

class OperatorAdmin(admin.ModelAdmin):
	list_display = ('name', 'logo', 'status')


admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Fleet)
admin.site.register(Manufacturer)
admin.site.register(Operator, OperatorAdmin)


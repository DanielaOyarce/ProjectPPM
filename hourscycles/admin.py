from django.contrib import admin
from .models import Hourscycles

class HourscyclesAdmin(admin.ModelAdmin):
	list_display = ('aircraft', 'flight_hours', 'block_hours', 'cycles', 'tsn', 'csn', 'nonrevenue_cycles', 'days_flown', 'date')	


admin.site.register(Hourscycles, HourscyclesAdmin)


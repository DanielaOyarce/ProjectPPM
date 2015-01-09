from django.db import models
from aircraft.models import Aircraft




class Hourscycles(models.Model):
	aircraft = models.ForeignKey(Aircraft) 
	flight_hours = models.FloatField(blank=True, null=True)
	block_hours = models.FloatField(blank=True, null=True)
	cycles = models.IntegerField(blank=True, null=True)
	tsn = models.FloatField(blank=True, null=True)
	csn = models.IntegerField(blank=True, null=True)
	nonrevenue_cycles = models.IntegerField(blank=True, null=True)
	days_flown = models.IntegerField(blank=True, null=True)
	date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.date



from django.db import models
from aircraft.models import Aircraft


class Mapi(models.Model):
	aircraft = models.ForeignKey(Aircraft)
	ata = models.IntegerField(blank=True, null=True)
	subata = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True, null=True)
	nmfl = models.CharField(max_length=20, blank=True, null=True)
	dtlmfl = models.DateTimeField(blank=True, null=True)
	flight_number = models.CharField(max_length=20, blank=True, null=True)
	sta = models.CharField(max_length=50, blank=True, null=True) 
	reference_term = models.CharField(max_length=50)
	nri = models.CharField(unique=True, max_length=20)
	dmi = models.CharField(max_length=20, blank=True, null=True)
	cat = models.CharField(max_length=20, blank=True, null=True) 
	duedate = models.DateTimeField(blank=True, null=True)
	discrepancies = models.TextField(blank=True, null=True)
	action_correct = models.TextField(blank=True, null=True)
	part_number = models.TextField(blank=True, null=True)
	position = models.CharField(max_length=100,blank=True, null=True)
	status = models.CharField(max_length=20)
	found_on_date = models.DateTimeField(blank=True, null=True)
	
	def __str__(self):
		return self.aircraft	



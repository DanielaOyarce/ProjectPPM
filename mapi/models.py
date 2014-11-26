from django.db import models
from aircraft.models import Aircraft


class Mapi(models.Model):
	aircraft = models.ForeignKey(Aircraft)
	ata = models.IntegerField()
	subAta = models.IntegerField()
	week = models.IntegerField(blank=True, null=True)
	nmfl = models.CharField(max_length=20, blank=True, null=True)
	dtlmfl = models.DateTimeField(blank=True, null=True)
	flightNumber = models.CharField(max_length=20, blank=True, null=True)
	sta = models.CharField(max_length=50, blank=True, null=True) 
	referenceTerm = models.CharField(max_length=50)
	nri = models.CharField(max_length=20, unique=True)
	dmi = models.CharField(max_length=20, blank=True, null=True)
	cat = models.CharField(max_length=20, blank=True, null=True) 
	dueDate = models.DateTimeField(blank=True, null=True)
	discrepancies = models.CharField(max_length=100)
	actionCorrect = models.CharField(max_length=100)
	partNumber = models.CharField(max_length=20, blank=True, null=True)
	position = models.IntegerField(blank=True, null=True)
	status = models.CharField(max_length=20)
	foundOnDate = models.DateTimeField()
	
		



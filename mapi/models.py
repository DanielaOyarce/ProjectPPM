from django.db import models
from aircraft.models import Aircraft


class Mapi(models.Model):
	aircraft = models.ForeignKey(Aircraft)
	ata = models.IntegerField()
	subAta = models.IntegerField()
	week = models.IntegerField()
	nmfl = models.CharField(max_length=20)
	dtlmfl = models.DateTimeField()
	flightNumber = models.CharField(max_length=20)
	sta = models.CharField(max_length=50) 
	referenceTerm = models.CharField(max_length=50)
	nri = models.CharField(max_length=20)
	dmi = models.CharField(max_length=20)
	cat = models.CharField(max_length=20) 
	dueDate = models.DateTimeField()
	discrepancies = models.CharField(max_length=100)
	actionCorrect = models.CharField(max_length=100)
	partNumber = models.CharField(max_length=20)
	position = models.IntegerField()
	status = models.CharField(max_length=20)
	foundOnDate = models.DateTimeField()
	def __str__(self):
		return self.aircraft
		



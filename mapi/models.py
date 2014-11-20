from django.db import models
from django.contrib import admin

class Mapi(models.Model):
	aircraft = models.CharField(max_length = 20)
	ata = models.IntegerField()
	subAta = models.IntegerField()
	week = models.IntegerField()
	nmfl = models.CharField(max_length = 20)
	dtlmfl = models.DateTimeField()
	flightNumber = models.CharField(max_length = 20)
	sta = models.CharField(max_length = 50) 
	referenceTerm = models.CharField(max_length = 50)
	nri = models.CharField(max_length = 20)
	dmi = models.CharField(max_length = 20)
	cat = models.CharField(max_length = 20) 
	dueDate = models.DateTimeField()
	discrepancies = models.CharField(max_length = 100)
	actionCorrect = models.CharField(max_length = 100)
	partNumber = models.CharField(max_length = 20)
	position = models.IntegerField()
	status = models.CharField(max_length = 20)
	foundOnDate = models.DateTimeField()

#class Mapi(admin.ModelAdmin): Para arreglar el modulo administrativo

		

admin.site.register(Mapi)
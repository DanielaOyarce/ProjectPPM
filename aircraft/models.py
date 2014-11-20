from django.db import models
from django.contrib import admin

class aircraft(models.Model):
	nameAircraft = models.CharField(max_length = 20)
	status = models.IntegerField()

class fleet(models.Model):
	nameFleet = models.CharField(max_length = 20)
	status = models.IntegerField()

class manufacturer(models.Model):
	nameManufacturer = models.CharField(max_length = 20)
	status = models.IntegerField()

class operator(models.Model):
	nameOperator = models.CharField(max_length = 20)
	logo = models.ImageField(upload_to='logos')
	status = models.IntegerField()

admin.site.register(aircraft)
admin.site.register(fleet)
admin.site.register(manufacturer)
admin.site.register(operator)
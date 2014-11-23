from django.db import models
from django.contrib import admin




class manufacturer(models.Model):
	name = models.CharField(max_length = 20)
	status = models.IntegerField()


class fleet(models.Model):
	manufacturer = models.ForeignKey(manufacturer)
	name = models.CharField(max_length = 20)
	status = models.IntegerField()


class operator(models.Model):
	name = models.CharField(max_length = 20)
	logo = models.ImageField(upload_to='logos')
	status = models.IntegerField()
		

class aircraft(models.Model):
	operator = models.ManyToManyField(operator)
	name = models.CharField(max_length = 20)
	fleet = models.ForeignKey(fleet)
	status = models.IntegerField()



admin.site.register(aircraft)
admin.site.register(fleet)
admin.site.register(manufacturer)
admin.site.register(operator)
from django.db import models


class Manufacturer(models.Model):
	name = models.CharField(max_length=20)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name

class Fleet(models.Model):
	manufacturer = models.ForeignKey(Manufacturer)
	name = models.CharField(max_length=20)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name



class Operator(models.Model):
	name = models.CharField(max_length=20)
	logo = models.ImageField(upload_to='logos')
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name

		

class Aircraft(models.Model):
	fleet = models.ForeignKey(Fleet)
	operator = models.ManyToManyField(Operator)
	name = models.CharField(max_length=20)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name



from django.db import models


class Manufacturer(models.Model):
	name = models.CharField(max_length=20, unique=True)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name


class Fleet(models.Model):
	name = models.CharField(max_length=20, unique=True)
	manufacturer = models.ForeignKey(Manufacturer)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name


class Operator(models.Model):
	name = models.CharField(max_length=20, unique=True)
	logo = models.ImageField(upload_to='logos')
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name
		

class Aircraft(models.Model):
	name = models.CharField(max_length=20, unique=True)
	fleet = models.ForeignKey(Fleet)
	operator = models.ManyToManyField(Operator)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name



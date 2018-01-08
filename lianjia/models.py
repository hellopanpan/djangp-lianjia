from django.db import models

class person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	def __str__(self):
		return self.name
# Create your models here.

class Area(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	position = models.CharField(max_length=20)
	def __str__(self):
		return self.name
class Login(models.Model):
	name = models.CharField(max_length=20)
	password = models.CharField(max_length = 20)
	def __str__(self):
		return self.name
class Lianjia(models.Model):
	title = models.CharField(max_length=100)
	img = models.CharField(max_length=100)
	link = models.CharField(max_length=100)
	position = models.CharField(max_length=30)
	floor = models.CharField(max_length=30)
	totlePrice = models.CharField(max_length=30)
	Price = models.CharField(max_length=30)
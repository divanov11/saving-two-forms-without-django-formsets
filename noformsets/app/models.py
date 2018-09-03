from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Product(models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank=True, null=True)
	product = models.CharField(max_length=200, blank=True, null=True, default=None)

	def __str__(self):
		return self.product

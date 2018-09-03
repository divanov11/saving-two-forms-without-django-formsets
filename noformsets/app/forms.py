from django import forms
from django.forms import ModelForm
from .models import *

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
		exclude  = ['customer']

from django.shortcuts import render
from .forms import *

def index(request):
	customerform = CustomerForm()
	productform = ProductForm()

	if request.POST:

		customer = Customer.objects.create(
			name = request.POST['name']
			)
		products = request.POST.getlist('product')

		for product in products:
			if product != '':
				Product.objects.create(
					customer = customer,
					product = product
					)
	


	context = {'customerform':customerform, 'productform':productform}
	return render(request, 'app/index.html', context)

def update(request, pk):

	customer = Customer.objects.get(id=pk)
	products = customer.product_set.all()

	customerform = CustomerForm(instance=customer)
	productform = ProductForm()

	if request.POST:
		print(request.POST)
		customerform = CustomerForm(request.POST, instance=customer)
		if customerform.is_valid():
			customerform.save()

		products = request.POST.getlist('product')

		for product in products:
			if product != '':
				Product.objects.create(
					customer = customer,
					product = product
					)

	context = {'products':products, 'customerform':customerform, 'productform':productform, 'customer':customer}
	return render(request, 'app/update_form.html', context)

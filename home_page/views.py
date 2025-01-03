from itertools import product

from django.shortcuts import render
from product.models import ProductCategories
from product.models import Product
# Create your views here.

def load_home_page(request):
    product_categoreies = ProductCategories.objects.all()
    products = Product.objects.all()
    context = {'product_categoreies': product_categoreies,
               'products': products}
    return render(request, 'home_page/index.html', context)

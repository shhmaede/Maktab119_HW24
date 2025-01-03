from pprint import pprint

from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategories


# Create your views here.
def show_all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home_page/index.html', context)

def show_product_details(request, product_id):
    #product = Product.objects.get(pk=product_id)
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)

def find_product_with_category(request, category_id):
    #products = Product.objects.filter(product_category_id=category_id)
    product_categoreies = ProductCategories.objects.all()
    category = ProductCategories.objects.get(id=category_id)
    products = category.products.all()
    context = {'product_categoreies': product_categoreies,
               'products': products}
    return render(request, 'home_page/index.html', context)

def find_product_with_name(request, product_name):
    #product_name = request.GET.get('product_name', 'Not provided')
    product_categoreies = ProductCategories.objects.all()
    products = Product.objects.filter(product_name__contains=product_name).values()
    pprint(products)
    context = {'product_categoreies': product_categoreies,
               'products': products}
    pprint(products)
    return render(request, 'home_page/index.html', context)


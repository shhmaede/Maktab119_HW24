from django.contrib import admin
from .models import Product
from .models import ProductCategories
from .models import Category

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)

class ProductCategoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductCategories, ProductCategoriesAdmin)


admin.site.register(Category)
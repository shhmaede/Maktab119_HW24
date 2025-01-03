from django.db import models
from django.db.models import Index
from django.urls import reverse


class ProductCategories(models.Model):
    category_name = models.CharField(max_length=63, db_column='category_name', null=False)

    def __str__(self):
        return f'{self.id}_{self.category_name}'

    def get_absolute_url(self):
        return reverse('load_product_categories', args=[self.id])

    class Meta:
        db_table = 'product_categories'
        ordering = ["-category_name"]
        #managed = False

class Product(models.Model):
    product_name = models.CharField('نام محصول', max_length=63, db_column='p_name', null=False)
    product_price = models.FloatField(db_column='product_price', null=False)
    product_description = models.CharField(max_length=512, db_column='product_description')
    product_image = models.ImageField(upload_to="images/", db_column='product_image')
    recorde_datetime = models.DateTimeField(db_column='recorde_datetime',auto_now_add=True, blank=True)
    product_category = models.ForeignKey(ProductCategories, on_delete=models.DO_NOTHING, db_column='product_category',
                                         related_name='products', related_query_name='category_id')
    Index(name='IX_RecordeDate', fields=['recorde_datetime'],
          include=['product_price', 'product_description', 'product_image', 'product_category'])

    def __str__(self):
        return f'{self.product_name}'

    def get_absolute_url(self):
        return reverse('load_product', args=[self.id])

    class Meta:
        db_table = 'products'
        ordering = ["product_name"]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


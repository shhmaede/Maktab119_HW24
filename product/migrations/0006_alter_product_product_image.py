# Generated by Django 4.2 on 2024-12-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(db_column='product_image', upload_to='images/'),
        ),
    ]
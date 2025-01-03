# Generated by Django 4.2 on 2024-12-31 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_productcategories_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_name'], 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(db_column='p_name', max_length=63, verbose_name='نام محصول'),
        ),
    ]

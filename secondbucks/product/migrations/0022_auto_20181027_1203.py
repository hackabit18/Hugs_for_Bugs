# Generated by Django 2.0.6 on 2018-10-27 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='product_image'),
        ),
    ]
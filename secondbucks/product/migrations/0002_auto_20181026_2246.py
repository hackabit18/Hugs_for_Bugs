# Generated by Django 2.0.6 on 2018-10-27 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='college',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wisher',
            name='category',
        ),
        migrations.RemoveField(
            model_name='wisher',
            name='college',
        ),
        migrations.RemoveField(
            model_name='wisher',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Wisher',
        ),
    ]

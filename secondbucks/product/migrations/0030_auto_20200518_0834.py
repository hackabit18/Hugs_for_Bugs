# Generated by Django 2.2.10 on 2020-05-18 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_auto_20200518_0617'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='College',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='college',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='college',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='wisher',
            old_name='college',
            new_name='state',
        ),
    ]

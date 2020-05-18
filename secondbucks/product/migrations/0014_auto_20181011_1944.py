# Generated by Django 2.0.6 on 2018-10-12 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20181009_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='college',
            name='state',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.College'),
        ),
    ]

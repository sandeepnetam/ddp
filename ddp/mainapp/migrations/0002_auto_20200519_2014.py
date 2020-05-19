# Generated by Django 3.0.6 on 2020-05-19 14:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseyear',
            name='name',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator('^[20]{2}\\d{2}[-][0-9]{2}$', 'Year Pattern is like yyyy-yy')], verbose_name='Base Year'),
        ),
        migrations.AlterField(
            model_name='year',
            name='name',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator('^[20]{2}\\d{2}[-][0-9]{2}$', 'Year Pattern is like yyyy-yy')], verbose_name='Year'),
        ),
    ]
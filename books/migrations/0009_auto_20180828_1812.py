# Generated by Django 2.1 on 2018-08-28 18:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20180828_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='no_pages',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Number of pages'),
        ),
    ]
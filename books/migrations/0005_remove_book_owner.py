# Generated by Django 2.1 on 2018-08-28 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20180828_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='owner',
        ),
    ]

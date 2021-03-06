# Generated by Django 2.1 on 2018-08-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('summary', models.TextField()),
                ('pages', models.CharField(max_length=60)),
                ('status', models.BooleanField()),
            ],
        ),
    ]

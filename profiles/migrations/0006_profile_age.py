# Generated by Django 3.1.1 on 2020-09-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200913_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(default='some age', max_length=5),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160806_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20160622_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='logo'),
        ),
    ]
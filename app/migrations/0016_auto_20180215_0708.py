# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180214_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='day',
            field=models.DateField(default=datetime.datetime(2018, 2, 15, 7, 8, 39, 940364)),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0009_defaultvalues_author_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultvalues',
            name='threshold_report',
            field=models.PositiveIntegerField(default=10),
        ),
    ]

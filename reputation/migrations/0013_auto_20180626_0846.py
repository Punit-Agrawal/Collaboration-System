# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0012_auto_20180621_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultvalues',
            name='comment_flag',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='downvote',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='min_crep_for_art',
            field=models.PositiveIntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='min_srep_for_comm',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='published_author',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='published_publisher',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='reply',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='srep_for_comm_creation',
            field=models.PositiveIntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='defaultvalues',
            name='upvote',
            field=models.PositiveIntegerField(default=2),
        ),
    ]

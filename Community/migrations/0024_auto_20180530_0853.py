# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 08:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0023_auto_20180530_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitycourses',
            name='community',
        ),
        migrations.AlterField(
            model_name='community',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitycreator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='communityarticles',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communityarticles', to='BasicArticle.Articles'),
        ),
        migrations.AlterField(
            model_name='communityarticles',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communityarticles', to='Community.Community'),
        ),
        migrations.AlterField(
            model_name='communityarticles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communityarticles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='communitycourses',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitycourses', to='Course.Course'),
        ),
        migrations.AlterField(
            model_name='communitycourses',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitycourses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='communitygroups',
            name='community',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitygroups', to='Community.Community'),
        ),
        migrations.AlterField(
            model_name='communitygroups',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitygroups', to='Group.Group'),
        ),
        migrations.AlterField(
            model_name='communitygroups',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitygroups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='communitymembership',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communitymembership', to='Community.Community'),
        ),
        migrations.AlterField(
            model_name='communitymembership',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitymembership', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='communitymembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communitymembership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requestcommunitycreation',
            name='requestedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
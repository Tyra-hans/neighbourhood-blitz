# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-12-03 12:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hoodapp', '0003_business_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

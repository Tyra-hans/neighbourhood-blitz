# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-12-02 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_post_post_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='profile_pic',
            field=models.ImageField(default='media/images/default.jpeg', upload_to='images/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-27 16:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180326_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 16, 49, 44, 598703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 16, 49, 44, 597703, tzinfo=utc)),
        ),
    ]
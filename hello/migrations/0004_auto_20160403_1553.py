# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20160403_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='haiku_arch',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='device',
            name='haiku_revision',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]

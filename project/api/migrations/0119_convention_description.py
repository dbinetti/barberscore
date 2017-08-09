# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0118_auto_20170807_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='convention',
            name='description',
            field=models.TextField(blank=True, help_text='\n            A general description field; usually used for hotel and venue info.', max_length=1000),
        ),
    ]

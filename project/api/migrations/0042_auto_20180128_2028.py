# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-29 04:28
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_auto_20180128_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(-20, 'Finished'), (-10, 'Missed'), (0, 'New'), (10, 'Made'), (20, 'Started')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.'),
        ),
    ]

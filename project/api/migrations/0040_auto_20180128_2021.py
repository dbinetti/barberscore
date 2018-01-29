# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-29 04:21
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_competitor_is_ranked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(-10, 'Finished'), (0, 'New'), (10, 'Started')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.'),
        ),
    ]

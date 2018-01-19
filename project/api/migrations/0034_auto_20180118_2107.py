# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-19 05:07
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20180113_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(0, 'New'), (5, 'Invited'), (7, 'Withdrawn'), (10, 'Submitted'), (20, 'Approved'), (52, 'Scratched'), (55, 'Disqualified')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.'),
        ),
    ]

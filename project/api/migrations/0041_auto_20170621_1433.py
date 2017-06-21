# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20170621_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='bhs_id',
        ),
        migrations.AlterField(
            model_name='appearance',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='chart',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='contest',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='convention',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='entity',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='entry',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='office',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='officer',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='participant',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='repertory',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='round',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='score',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='session',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='slot',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='venue',
            name='nomen',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]

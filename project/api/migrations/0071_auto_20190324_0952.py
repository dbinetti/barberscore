# Generated by Django 2.1.7 on 2019-03-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0070_award_is_single'),
    ]

    operations = [
        migrations.AddField(
            model_name='appearance',
            name='is_single',
            field=models.BooleanField(default=False, help_text='Single-round contestant'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='is_single',
            field=models.BooleanField(default=False, help_text='Single-round competitor'),
        ),
    ]

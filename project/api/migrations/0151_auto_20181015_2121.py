# Generated by Django 2.1.2 on 2018-10-16 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0150_auto_20181015_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selection',
            old_name='draw',
            new_name='appearance_num',
        ),
        migrations.RenameField(
            model_name='selection',
            old_name='num',
            new_name='song_num',
        ),
        migrations.RenameField(
            model_name='selection',
            old_name='legacy_chart',
            new_name='song_title',
        ),
    ]

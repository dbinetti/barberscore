# Generated by Django 2.1.2 on 2018-10-08 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0129_auto_20181007_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='complete',
            name='season',
            field=models.IntegerField(blank=True, choices=[(1, 'Summer'), (2, 'Midwinter'), (3, 'Fall'), (4, 'Spring'), (9, 'Video')], null=True),
        ),
    ]
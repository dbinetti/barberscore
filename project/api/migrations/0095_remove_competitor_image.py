# Generated by Django 2.1.7 on 2019-03-28 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0094_auto_20190328_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitor',
            name='image',
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-25 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bhs', '0006_auto_20190725_1602'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='officer',
            unique_together=set(),
        ),
    ]
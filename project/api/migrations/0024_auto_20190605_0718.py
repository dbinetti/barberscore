# Generated by Django 2.1.8 on 2019-06-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_remove_outcome_is_primary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='spots',
            field=models.IntegerField(default=0),
        ),
    ]
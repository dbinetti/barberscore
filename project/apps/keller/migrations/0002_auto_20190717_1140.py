# Generated by Django 2.2.3 on 2019-07-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complete',
            name='person',
        ),
        migrations.AddField(
            model_name='complete',
            name='person_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
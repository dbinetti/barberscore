# Generated by Django 2.1.8 on 2019-05-17 17:00

from django.db import migrations


def forward(apps, schema_editor):
    Old = apps.get_model('api.convention')
    New = apps.get_model('cmanager.convention')

    items = Old.objects.values()
    for item in items:
        New.objects.create(**item)

    Old = apps.get_model('api.award')
    New = apps.get_model('cmanager.award')

    items = Old.objects.values()
    for item in items:
        New.objects.create(**item)

    Old = apps.get_model('api.assignment')
    New = apps.get_model('cmanager.assignment')

    items = Old.objects.values()
    for item in items:
        New.objects.create(**item)




class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190517_1019'),
        ('cmanager', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward),
    ]

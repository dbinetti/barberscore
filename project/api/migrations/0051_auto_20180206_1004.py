# Generated by Django 2.0.2 on 2018-02-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_officer_bhs_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='kind',
            field=models.IntegerField(choices=[('International', [(1, 'International')]), ('District', [(11, 'District'), (12, 'Noncompetitive'), (13, 'Affiliate')]), ('Division', [(21, 'Division')]), ('Chapter', [(30, 'Chapter')]), ('Group', [(32, 'Chorus'), (41, 'Quartet')])], help_text='\n            The kind of organization.\n        '),
        ),
    ]

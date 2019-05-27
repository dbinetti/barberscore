# Generated by Django 2.1.8 on 2019-05-26 19:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keller', '0008_auto_20190526_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawSong',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('season', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('district', models.CharField(max_length=255)),
                ('event', models.CharField(max_length=255)),
                ('session', models.CharField(max_length=255)),
                ('group_name', models.CharField(max_length=255)),
                ('appearance_num', models.IntegerField()),
                ('song_num', models.IntegerField()),
                ('song_title', models.CharField(max_length=255)),
                ('totals', models.IntegerField()),
                ('scores', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]

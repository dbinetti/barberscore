# Generated by Django 2.1.2 on 2018-10-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0166_auto_20181018_0646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selection',
            old_name='district',
            new_name='district_code',
        ),
        migrations.AddField(
            model_name='selection',
            name='district_raw',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
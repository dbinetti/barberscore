# Generated by Django 2.1.2 on 2018-10-29 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0196_auto_20181029_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='contender',
            name='outcome',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contenders', to='api.Outcome'),
        ),
        migrations.AlterUniqueTogether(
            name='contender',
            unique_together={('appearance', 'outcome')},
        ),
    ]

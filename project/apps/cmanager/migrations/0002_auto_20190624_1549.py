# Generated by Django 2.1.9 on 2019-06-24 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmanager', '0001_initial'),
        ('bhs', '0001_initial'),
        ('stage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='convention',
            name='venue',
            field=models.ForeignKey(blank=True, help_text='\n            The specific venue for the convention (if available.)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conventions', to='stage.Venue'),
        ),
        migrations.AddField(
            model_name='award',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='bhs.Group'),
        ),
        migrations.AddField(
            model_name='award',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='If a qualifier, this is the award qualifying for.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='cmanager.Award'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='convention',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='cmanager.Convention'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignments', to='bhs.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='convention',
            unique_together={('year', 'season', 'name', 'group')},
        ),
    ]

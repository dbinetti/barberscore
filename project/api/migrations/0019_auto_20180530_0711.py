# Generated by Django 2.0.5 on 2018-05-30 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.Person'),
        ),
    ]

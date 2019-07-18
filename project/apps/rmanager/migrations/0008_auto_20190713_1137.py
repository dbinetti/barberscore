# Generated by Django 2.2.3 on 2019-07-13 18:37

from django.db import migrations

def forward(apps, schema_editor):
    Round = apps.get_model('rmanager.round')
    Person = apps.get_model('bhs.person')
    User = apps.get_model('rest_framework_jwt.user')

    rs = Round.objects.filter(
        session__convention__assignments__isnull=False,
    )
    for r in rs:
        assignments = r.session.convention.assignments.filter(
            category=10,
        ).distinct()
        for assignment in assignments:
            try:
                person = Person.objects.get(id=assignment.person_id)
            except Person.DoesNotExist:
                continue
            if not person.email:
                continue
            try:
                user = User.objects.get(
                    email=person.email,
                )
            except User.DoesNotExist:
                continue
            r.owners.add(user)


class Migration(migrations.Migration):

    dependencies = [
        ('rmanager', '0007_auto_20190713_1129'),
    ]

    operations = [
        migrations.RunPython(forward)
    ]

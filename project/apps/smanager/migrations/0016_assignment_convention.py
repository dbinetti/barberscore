# Generated by Django 2.2.3 on 2019-07-19 18:20

import apps.smanager.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smanager', '0015_auto_20190719_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convention',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (5, 'Built'), (10, 'Active')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('name', models.CharField(default='Convention', max_length=255)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('season', models.IntegerField(choices=[(3, 'Fall'), (4, 'Spring')])),
                ('panel', models.IntegerField(blank=True, choices=[(1, 'Single'), (2, 'Double'), (3, 'Triple'), (4, 'Quadruple'), (5, 'Quintiple')], null=True)),
                ('year', models.IntegerField(choices=[(2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939)])),
                ('open_date', models.DateField(blank=True, null=True)),
                ('close_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('venue_name', models.CharField(default='(TBD)', help_text='\n            The venue name (when available).', max_length=255)),
                ('location', models.CharField(default='(TBD)', help_text='\n            The general location in the form "City, State".', max_length=255)),
                ('timezone', timezone_field.fields.TimeZoneField(blank=True, help_text='\n            The local timezone of the convention.', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.smanager.fields.ImageUploadPath())),
                ('description', models.TextField(blank=True, help_text='\n            A general description field; usually used for hotel and venue info.', max_length=1000)),
                ('divisions', apps.smanager.fields.DivisionsField(base_field=models.IntegerField(choices=[('EVG', [(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V')]), ('FWD', [(60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest')]), ('LOL', [(110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest')]), ('MAD', [(170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern')]), ('NED', [(210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee')]), ('SWD', [(260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')])]), blank=True, default=list, help_text='Only select divisions if required.  If it is a district-wide convention do not select any.', size=None)),
                ('kinds', apps.smanager.fields.DivisionsField(base_field=models.IntegerField(choices=[(32, 'Chorus'), (41, 'Quartet'), (42, 'Mixed'), (43, 'Senior'), (44, 'Youth'), (45, 'Unknown'), (46, 'VLQ')]), blank=True, default=list, help_text='The session kind(s) created at build time.', size=None)),
                ('group_id', models.UUIDField(blank=True, null=True)),
                ('owners', models.ManyToManyField(related_name='conventions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=10, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(10, 'Official'), (20, 'Practice'), (30, 'Observer')])),
                ('category', models.IntegerField(blank=True, choices=[(5, 'DRCJ'), (10, 'CA'), (30, 'Music'), (40, 'Performance'), (50, 'Singing')], null=True)),
                ('person_id', models.UUIDField(blank=True, null=True)),
                ('convention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='smanager.Convention')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

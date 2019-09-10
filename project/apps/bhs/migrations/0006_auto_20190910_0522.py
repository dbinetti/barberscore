# Generated by Django 2.2.5 on 2019-09-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhs', '0005_auto_20190909_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='district',
            field=models.IntegerField(choices=[('BHS', [(200, 'CAR'), (205, 'CSD'), (210, 'DIX'), (215, 'EVG'), (220, 'FWD'), (225, 'ILL'), (230, 'JAD'), (235, 'LOL'), (240, 'MAD'), (345, 'NED'), (350, 'NSC'), (355, 'ONT'), (360, 'PIO'), (365, 'RMD'), (370, 'SLD'), (375, 'SUN'), (380, 'SWD')]), ('Associated', [(410, 'NxtGn'), (420, 'MBHA'), (430, 'HI'), (440, 'SAI')]), ('Affiliated', [(510, 'BABS'), (515, 'BHA'), (520, 'BHNZ'), (525, 'BinG'), (530, 'FABS'), (540, 'HHar'), (550, 'IABS'), (560, 'LABBS'), (565, 'SABS'), (570, 'SNOBS'), (575, 'SPATS')])]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0004_auto_20141202_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hourscycles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flight_hours', models.FloatField()),
                ('block_hours', models.FloatField()),
                ('cycles', models.IntegerField()),
                ('tsn', models.FloatField()),
                ('csn', models.IntegerField()),
                ('nonrevenue_cycles', models.IntegerField()),
                ('days_flown', models.IntegerField()),
                ('aircraft', models.ForeignKey(to='aircraft.Aircraft')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

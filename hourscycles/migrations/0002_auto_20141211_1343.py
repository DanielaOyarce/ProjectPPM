# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hourscycles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourscycles',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hourscycles',
            name='block_hours',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hourscycles',
            name='csn',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hourscycles',
            name='cycles',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hourscycles',
            name='days_flown',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hourscycles',
            name='flight_hours',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hourscycles',
            name='nonrevenue_cycles',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hourscycles',
            name='tsn',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

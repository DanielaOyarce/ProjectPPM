# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0003_auto_20141126_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='operator',
            field=models.ManyToManyField(to='aircraft.Operator', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fleet',
            name='manufacturer',
            field=models.ForeignKey(blank=True, to='aircraft.Manufacturer', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operator',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'logos', blank=True),
            preserve_default=True,
        ),
    ]

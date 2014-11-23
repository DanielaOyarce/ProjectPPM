# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aircraft',
            old_name='nameAircraft',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='fleet',
            old_name='nameFleet',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='nameManufacturer',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='operator',
            old_name='nameOperator',
            new_name='name',
        ),
    ]

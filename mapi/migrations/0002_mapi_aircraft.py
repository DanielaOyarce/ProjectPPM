# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0002_auto_20141124_1137'),
        ('mapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapi',
            name='aircraft',
            field=models.ForeignKey(default=1, to='aircraft.Aircraft'),
            preserve_default=False,
        ),
    ]

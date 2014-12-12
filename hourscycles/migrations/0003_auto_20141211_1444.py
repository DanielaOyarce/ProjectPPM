# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hourscycles', '0002_auto_20141211_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourscycles',
            name='cicles_rent',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hourscycles',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0003_auto_20141126_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapi',
            name='subAta',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

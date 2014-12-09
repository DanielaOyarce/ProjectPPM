# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0011_auto_20141209_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapi',
            name='ata',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

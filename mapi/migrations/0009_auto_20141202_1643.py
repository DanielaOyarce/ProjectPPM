# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0008_auto_20141202_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapi',
            name='position',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0009_auto_20141202_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapi',
            name='actionCorrect',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mapi',
            name='discrepancies',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

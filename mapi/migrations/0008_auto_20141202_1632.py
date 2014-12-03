# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0007_auto_20141202_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapi',
            name='partNumber',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

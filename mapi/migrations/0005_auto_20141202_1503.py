# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0004_auto_20141202_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapi',
            name='dtlmfl',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mapi',
            name='dueDate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mapi',
            name='foundOnDate',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]

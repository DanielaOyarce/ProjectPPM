# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0005_auto_20141202_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapi',
            name='actionCorrect',
            field=models.TextField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mapi',
            name='discrepancies',
            field=models.TextField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mapi',
            name='dtlmfl',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mapi',
            name='dueDate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mapi',
            name='foundOnDate',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]

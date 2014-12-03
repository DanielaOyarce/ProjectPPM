# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0006_auto_20141202_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapi',
            name='actionCorrect',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mapi',
            name='discrepancies',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

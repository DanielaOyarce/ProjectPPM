# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hourscycles', '0003_auto_20141211_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hourscycles',
            name='cicles_rent',
        ),
    ]

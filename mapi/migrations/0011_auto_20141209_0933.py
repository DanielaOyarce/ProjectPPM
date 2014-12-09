# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0010_auto_20141203_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mapi',
            old_name='actionCorrect',
            new_name='action_correct',
        ),
        migrations.RenameField(
            model_name='mapi',
            old_name='dueDate',
            new_name='duedate',
        ),
        migrations.RenameField(
            model_name='mapi',
            old_name='flightNumber',
            new_name='flight_number',
        ),
        migrations.RenameField(
            model_name='mapi',
            old_name='partNumber',
            new_name='part_number',
        ),
        migrations.RenameField(
            model_name='mapi',
            old_name='referenceTerm',
            new_name='reference_term',
        ),
        migrations.RenameField(
            model_name='mapi',
            old_name='subAta',
            new_name='subata',
        ),
        migrations.RemoveField(
            model_name='mapi',
            name='foundOnDate',
        ),
        migrations.AddField(
            model_name='mapi',
            name='found_on_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

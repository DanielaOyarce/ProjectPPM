# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mapi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ata', models.IntegerField()),
                ('subAta', models.IntegerField()),
                ('week', models.IntegerField()),
                ('nmfl', models.CharField(max_length=20)),
                ('dtlmfl', models.DateTimeField()),
                ('flightNumber', models.CharField(max_length=20)),
                ('sta', models.CharField(max_length=50)),
                ('referenceTerm', models.CharField(max_length=50)),
                ('nri', models.CharField(max_length=20)),
                ('dmi', models.CharField(max_length=20)),
                ('cat', models.CharField(max_length=20)),
                ('dueDate', models.DateTimeField()),
                ('discrepancies', models.CharField(max_length=100)),
                ('actionCorrect', models.CharField(max_length=100)),
                ('partNumber', models.CharField(max_length=20)),
                ('position', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('foundOnDate', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150204_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationInstruction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('location', models.OneToOneField(to='main.Location')),
                ('receiver', models.ForeignKey(to='main.Volunteer')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MessageInstruction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('receiver', models.ForeignKey(to='main.Volunteer')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

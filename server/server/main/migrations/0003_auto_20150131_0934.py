# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150131_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='category',
            field=models.ForeignKey(to='main.POICategory'),
            preserve_default=True,
        ),
    ]

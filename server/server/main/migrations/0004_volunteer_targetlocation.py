# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150131_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='targetLocation',
            field=models.OneToOneField(null=True, related_name='target', to='main.Location', blank=True),
            preserve_default=True,
        ),
    ]

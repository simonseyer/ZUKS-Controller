# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_locationinstruction_messageinstruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationinstruction',
            name='location',
            field=models.ForeignKey(to='main.Location'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='poi',
            name='location',
            field=models.ForeignKey(to='main.Location'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='location',
            field=models.ForeignKey(to='main.Location'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='targetLocation',
            field=models.ForeignKey(null=True, related_name='target', to='main.Location', blank=True),
            preserve_default=True,
        ),
    ]

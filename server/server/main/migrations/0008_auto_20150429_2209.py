# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150205_0307'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='volunteer',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]

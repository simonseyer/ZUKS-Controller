# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_volunteer_targetlocation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poi',
            options={'ordering': ['category', 'name']},
        ),
        migrations.AlterModelOptions(
            name='poicategory',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AlterModelOptions(
            name='volunteergroup',
            options={'ordering': ['name']},
        ),
    ]

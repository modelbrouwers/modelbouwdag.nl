# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='divider',
            name='label',
            field=models.CharField(default='divider', verbose_name='label', max_length=50),
            preserve_default=False,
        ),
    ]

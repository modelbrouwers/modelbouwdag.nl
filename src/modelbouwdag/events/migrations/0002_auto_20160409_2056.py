# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='date', unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.DecimalField(null=True, decimal_places=2, verbose_name='price', blank=True, max_digits=5),
        ),
    ]

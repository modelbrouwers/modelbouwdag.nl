# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0002_auto_20160409_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitorlistplugin',
            name='for_event',
            field=models.ForeignKey(to='events.Event', verbose_name='event'),
        ),
    ]

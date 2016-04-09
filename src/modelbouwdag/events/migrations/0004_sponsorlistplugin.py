# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('events', '0003_auto_20160409_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorListPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, to='cms.CMSPlugin', serialize=False)),
                ('for_event', models.ForeignKey(to='events.Event', verbose_name='event')),
            ],
            options={
                'verbose_name_plural': 'sponsor lists',
                'verbose_name': 'sponsor list',
            },
            bases=('cms.cmsplugin',),
        ),
    ]

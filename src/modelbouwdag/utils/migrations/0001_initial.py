# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Divider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, serialize=False, to='cms.CMSPlugin', parent_link=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'divider',
                'verbose_name_plural': 'dividers',
            },
            bases=('cms.cmsplugin',),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0013_urlconfrevision'),
        ('utils', '0002_divider_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, to='cms.CMSPlugin', primary_key=True, auto_created=True, parent_link=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('url', models.URLField(blank=True, help_text='has precedence over href', verbose_name='url')),
                ('href', models.CharField(max_length=255, blank=True, verbose_name='href')),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'menu items',
                'verbose_name': 'menu item',
            },
            bases=('cms.cmsplugin',),
        ),
    ]

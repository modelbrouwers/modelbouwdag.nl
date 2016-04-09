# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelbouwdag.exhibitors.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('events', '0002_auto_20160409_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibitor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='name', help_text='To embed links, use the following syntax: [text-for-the-link]({url}). You can enter an actual url, or leave the {url} placeholder, which will be replaced by the exhibitors url.')),
                ('url', models.URLField(verbose_name='url', blank=True)),
                ('description', models.CharField(max_length=500, verbose_name='description', help_text='To embed links, use the following syntax: [text-for-the-link]({url}). You can enter an actual url, or leave the {url} placeholder, which will be replaced by the exhibitors url.')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('event', models.ForeignKey(default=modelbouwdag.exhibitors.models.get_upcoming_event, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitorListPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('for_event', models.ForeignKey(to='events.Event')),
            ],
            options={
                'verbose_name_plural': 'exhibitor lists',
                'verbose_name': 'exhibitor list',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ExhibitorType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('code', models.CharField(max_length=10, verbose_name='code', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='types',
            field=models.ManyToManyField(to='exhibitors.ExhibitorType', verbose_name='types', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('events', '0002_auto_20160409_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('order', models.PositiveIntegerField(default=0)),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('url', models.URLField(verbose_name='url')),
                ('logo', filer.fields.image.FilerImageField(to='filer.Image', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'sponsor',
                'verbose_name_plural': 'sponsors',
            },
        ),
        migrations.AddField(
            model_name='eventsponsor',
            name='sponsor',
            field=models.ForeignKey(to='events.Sponsor'),
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(related_name='events', through='events.EventSponsor', blank=True, to='events.Sponsor'),
        ),
    ]

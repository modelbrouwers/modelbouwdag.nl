# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
        ('utils', '0004_facebookpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('extended_object', models.OneToOneField(to='cms.Page', editable=False)),
                ('image', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.Image', blank=True)),
                ('public_extension', models.OneToOneField(null=True, to='utils.IconExtension', related_name='draft_extension', editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

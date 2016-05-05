# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('utils', '0003_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, to='cms.CMSPlugin', serialize=False)),
                ('facebook_page_url', models.URLField(verbose_name='facebook page url')),
                ('tabs', models.CharField(default='timeline', max_length=255, verbose_name='tabs')),
                ('width', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(180), django.core.validators.MaxValueValidator(500)], null=True, blank=True, verbose_name='width')),
                ('height', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(70)], null=True, blank=True, verbose_name='height')),
                ('small_header', models.BooleanField(default=False, verbose_name='use small header')),
                ('hide_cover_photo', models.BooleanField(default=False, verbose_name='hide cover photo')),
                ('adapt_to_container_width', models.BooleanField(default=True, verbose_name='adapt to container width')),
                ('show_friends_faces', models.BooleanField(default=True, verbose_name="show friend's faces")),
            ],
            options={
                'verbose_name_plural': 'facebook page plugins',
                'verbose_name': 'facebook page plugin',
            },
            bases=('cms.cmsplugin',),
        ),
    ]

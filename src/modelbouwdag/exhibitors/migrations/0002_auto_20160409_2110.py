# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelbouwdag.exhibitors.models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitor',
            name='description',
            field=models.CharField(verbose_name='description', blank=True, help_text='To embed links, use the following syntax: [text-for-the-link]({url}). You can enter an actual url, or leave the {url} placeholder, which will be replaced by the exhibitors url.', max_length=500),
        ),
        migrations.AlterField(
            model_name='exhibitor',
            name='order',
            field=models.PositiveIntegerField(verbose_name='order', default=modelbouwdag.exhibitors.models.get_next_order),
        ),
    ]

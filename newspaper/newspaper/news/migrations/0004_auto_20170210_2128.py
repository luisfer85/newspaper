# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_event_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='No requerido', blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(help_text='No requerido', blank=True, null=True, verbose_name='description'),
        ),
    ]

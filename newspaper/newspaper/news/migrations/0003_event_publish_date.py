# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170210_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='publish_date',
            field=models.DateTimeField(default='2017-02-10 22:15', verbose_name='publish date'),
            preserve_default=False,
        ),
    ]

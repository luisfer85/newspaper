# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('cescription', models.TextField(verbose_name='description')),
                ('publish_date', models.DateTimeField(verbose_name='publish date')),
            ],
            options={
                'verbose_name': 'news item',
                'verbose_name_plural': 'news',
            },
        ),
    ]

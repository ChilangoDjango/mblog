# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150605_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=django_markdown.models.MarkdownField(),
        ),
    ]

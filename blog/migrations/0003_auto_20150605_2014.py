# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150605_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', editable=False, unique=True),
        ),
    ]

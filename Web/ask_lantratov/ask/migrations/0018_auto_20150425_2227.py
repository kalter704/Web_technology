# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0017_auto_20150425_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]

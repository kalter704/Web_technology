# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_auto_20150423_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
    ]

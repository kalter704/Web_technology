# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0005_userprofile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0013_auto_20150425_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

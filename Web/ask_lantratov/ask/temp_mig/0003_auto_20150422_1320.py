# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0002_question_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='ask.Tag'),
            preserve_default=True,
        ),
    ]

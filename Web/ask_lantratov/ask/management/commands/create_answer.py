# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
import datetime
from ask.models import Question, Tag, Answer
from django.contrib.auth.models import User

class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
		u = User.objects.get(id=1)
		q = Question.objects.get(id=8)
		a = Answer(question = q,
				   text = u'Новый ответ!)!)',
				   author = u,
				   )
		a.save()

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
		q = Question(title = u'Проверка',
					 text = u'Проверка работоспособности',
					 author = u,
					 rating = 79
					 )
		q.save()
		
        # Activate a fixed locale, e.g. Russian
        #translation.activate('ru')

        # Or you can activate the LANGUAGE_CODE # chosen in the settings:
        #
        #from django.conf import settings
        #translation.activate(settings.LANGUAGE_CODE)

        # Your command logic here
        # ...

        #translation.deactivate()

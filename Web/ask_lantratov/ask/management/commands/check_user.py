# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
import datetime
from ask.models import Question, Tag, Answer, UserProfile
from django.contrib.auth.models import User
import random, string

def randomword(start, end):
	return ''.join(random.choice(string.lowercase) for i in range(random.randint(start, end)))
	
def randomPassword(length):
	return ''.join(random.choice('0123456789') for i in range(length))

### Create User and Profile!!!!!!!!!!!!!!!!!!!!!
###
###	u_nickname - random
###	u_password - random
###	u_mail - u_title + @mail.ru
### 
### up_title = u_nickname
### up_user - relationship with User
### up_rating - random
### up_avater - later

class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
		u_nickname = raw_input('Nickname: ')
		is_exist = True
		try:
			u = User.objects.get(username = u_nickname)
		except:
			u = 'Пользователь "' + u_nickname + '" не зарегистрирован!'
			is_exist = False
		if is_exist:
			print('Пользователь: ')
		print(u)

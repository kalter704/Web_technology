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
		print('Create new USER!!!')
		u_nickname = raw_input('Nickname: ')
		u_password = raw_input('Password: ')
		u_mail = u_nickname + '@mail.ru'
		up_title = u_nickname;
		up_rating = random.randint(-15, 200)
		u = User.objects.create_user(u_nickname, u_mail, u_password)
		up = UserProfile(title = up_title, user = u, rating = up_rating, avatar = "NULL")
		up.save()
		print('New user is created!')
		
		#print('\nNickname: ' + u_nickname)
		#print('Password: ' + u_password)
		#print('Mail: ' + u_mail)
		#print('Title: ' + up_title)
		#print('Rating: ' + str(up_rating))
		
		#string_length_low = 4
		#string_length_high = 7
		#password_length = 8
		#number_user = 1

		#for i in range(number_user):
		#	u_nickname = randomword(string_length_low, string_length_high)
		#	u_password = randomPassword(password_length)
		#	u_mail = u_nickname + '@mail.ru'
		#	up_title = u_nickname;
		#	up_rating = random.randint(-15, 200)
		#	
		#	u = User.objects.create_user(u_nickname, u_mail, u_password)
		#	up = UserProfile(title = up_title, user = u, rating = up_rating, avatar = "NULL")
		#	up.save()
		#	if (i % 50 == 0):
		#		print('Created User #' + str(i))
		
		#print('Created User #' + str(number_user))

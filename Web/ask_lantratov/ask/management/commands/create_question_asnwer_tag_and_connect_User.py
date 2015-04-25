# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
import datetime
from ask.models import Question, Tag, Answer, UserProfile
from django.contrib.auth.models import User
import random, string

def randomword(start, end):
	return ''.join(random.choice(string.lowercase) for i in range(random.randint(start, end)))
	
def create_qusetion_answer_and_connect_user(how_many):
	for j in range(how_many):
		### User get random
		user_id = random.randint(1, 10362)
		try:
			u = User.objects.get(id=user_id)
		except:
			print('################################################################')
			print('USER DoesNotExist' + str(user_id))
			print('################################################################')
			return
		### End User get random
		
		### Tag create
		start_tag_lenght = 3
		end_tag_lenght = 6
		t_text = randomword(start_tag_lenght, end_tag_lenght)
		
		t = Tag(text = t_text)
		
		t.save()
		### End Tag create
		
		### Question create
		question_length_low = 8
		question_length_high = 15
		q_title = randomword(question_length_low, question_length_high)
		for i in range(random.randint(0, 2)):
			q_title = q_title + ' ' + randomword(question_length_low, question_length_high)
		q_title = q_title  + '?'
		q_text = randomword(question_length_low, question_length_high)
		for i in range(random.randint(3, 20)):
			q_text = q_text + ' ' + randomword(question_length_low, question_length_high)
		q_rating = random.randint(-10, 150)
		
		q = Question(title = q_title,
					 text = q_text,
					 author = u,
					 rating = q_rating
					 )
					 
		q.save()
		q.tags.add(t)
		q.save()
		### End Question create
		
		### User get random
		ser_id = random.randint(1, 10362)
		try:
			u = User.objects.get(id=user_id)
		except:
			print('################################################################')
			print('USER DoesNotExist' + str(user_id))
			print('################################################################')
			return
		### End User get random
		
		### Answer create
		answer_length_low = 8
		answer_length_high = 15
		a_text = randomword(answer_length_low, answer_length_high)
		for i in range(random.randint(7, 25)):
			a_text = a_text + ' ' + randomword(answer_length_low, answer_length_high)
		a_right_answer = True
		
		a = Answer(question = q,
				   text = a_text, 
				   right_answer = a_right_answer, 
				   author = u
				   )
		a.save()
		### End asnwer create
		print('Create: ' + str(j))
	print('Create: ' + str(how_many))
		
		
	
class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
		how_many = 50
		create_qusetion_answer_and_connect_user(how_many)

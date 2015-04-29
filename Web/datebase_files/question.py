# -*- coding: utf-8 -*-
from datetime import datetime
import time
import random, string

def randomword(start, end):
	return ''.join(random.choice(string.lowercase) for i in range(random.randint(start, end)))
	
question_length_low = 8
question_length_high = 15
number_question = 100100
number_users = 10099
#number_question = 10
f = open('question.txt', 'w')


for j in range(number_question):
	user_id = random.randint(1, number_users)
	q_title = randomword(question_length_low, question_length_high)
	for i in range(random.randint(0, 2)):
		q_title = q_title + ' ' + randomword(question_length_low, question_length_high)
	q_title = q_title  + '?'
	q_text = randomword(question_length_low, question_length_high)
	for i in range(random.randint(3, 20)):
		q_text = q_text + ' ' + randomword(question_length_low, question_length_high)
	q_rating = random.randint(-10, 150)
	#q_created = datetime.datetime.now
	
	m_rand = random.randint(1, 12)
	d_rand = random.randint(1, 28)
	H_rand = random.randint(0, 23)
	M_rand = random.randint(0, 59)
	S_rand = random.randint(0, 59)
	dt_obj = datetime(2015, m_rand, d_rand, H_rand, M_rand, S_rand)
	q_created = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
	
	question = q_title + '|' + q_text + '|' + str(user_id) + '|' + str(q_rating) + '|'+ str(q_created) + '\n'
	f.write(question)
	print('Created Question #' + str(j + 1))

f.close()

# -*- coding: utf-8 -*-
import datetime
import random, string

def randomword(start, end):
	return ''.join(random.choice(string.lowercase) for i in range(random.randint(start, end)))
	
answer_length_low = 8
answer_length_high = 15
number_answers = 1000100
#number_answers = 10
number_users = 10099
number_questions = 100100

f = open('answer.txt', 'w')
j = 0
while(j < number_questions):
	user_id = random.randint(1, number_users)
	question_id = j + 1
	a_text = randomword(answer_length_low, answer_length_high)
	for i in range(random.randint(7, 25)):
		a_text = a_text + ' ' + randomword(answer_length_low, answer_length_high)
	#a_right_answer = random.randint(0, 1)
	a_right_answer = 1
	
	answer = a_text + '|' + str(a_right_answer) + '|' + str(user_id) + '|' + str(question_id) + '\n'
	
	f.write(answer)
	print('Created Answer #' + str(j + 1))
	j += 1
	
while(j < number_answers):
	user_id = random.randint(1, number_users)
	question_id = random.randint(1, number_questions)
	a_text = randomword(answer_length_low, answer_length_high)
	for i in range(random.randint(7, 25)):
		a_text = a_text + ' ' + randomword(answer_length_low, answer_length_high)
	
	a_right_answer = 0
	if (random.randint(0, 7) == 7):
		a_right_answer = 1
		
	
	answer = a_text + '|' + str(a_right_answer) + '|' + str(user_id) + '|' + str(question_id) + '\n'
	
	f.write(answer)
	print('Created Answer #' + str(j + 1))
	j += 1

f.close()

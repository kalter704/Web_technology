# -*- coding: utf-8 -*-
import datetime
import random, string

def randomword(start, end):
	return ''.join(random.choice(string.lowercase) for i in range(random.randint(start, end)))

number_questions = 100100
number_tags = 10100
number_relationship = 300000

f = open('questions_tags.txt', 'w')
j = 0

while(j < number_tags):
	tag_id = j + 1
	question_id = j + 1
	relationship = str(question_id) + '|' + str(tag_id) + '\n'
	f.write(relationship)
	print('Created Relationship #' + str(j + 1))
	j += 1

while(j < number_questions):
	tag_id = random.randint(1, number_tags)
	question_id = j + 1
	relationship = str(question_id) + '|' + str(tag_id) + '\n'
	f.write(relationship)
	print('Created Relationship #' + str(j + 1))
	j += 1
	
while(j < number_relationship):
	tag_id = random.randint(1, number_tags)
	question_id = random.randint(1, number_questions)
	relationship = str(question_id) + '|' + str(tag_id) + '\n'
	f.write(relationship)
	print('Created Relationship #' + str(j + 1))
	j += 1
	
f.close()



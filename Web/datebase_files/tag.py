# -*- coding: utf-8 -*-
import datetime
import random, string

def randomword(start, end):
	return ''.join(random.choice(string.lowercase) for i in range(random.randint(start, end)))
	
number_questions = 100100
start_tag_lenght = 3
end_tag_lenght = 6
number_tags = 10100

f = open('tag.txt', 'w')

for j in range(number_tags):
	t_text = randomword(start_tag_lenght, end_tag_lenght)
	tag = t_text + '\n'
	f.write(tag)
	print('Created Tag #' + str(j + 1))

f.close()

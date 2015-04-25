# -*- coding: utf-8 -*-
import datetime
import random, string

def randomword(start, end):
	return ''.join(random.choice(string.lowercase) for i in range(random.randint(start, end)))
	
def randomPassword(length):
	return ''.join(random.choice('0123456789') for i in range(length))

name_length_low = 4
name_length_high = 7
password_length = 8
number_users = 10099

f_users = open('users.txt', 'w')
f_profiles = open('profiles.txt', 'w')

for i in range(number_users):
	u_nickname = randomword(name_length_low, name_length_high)
	u_nickname += str(i % 1000)
	u_password = randomPassword(password_length)
	u_mail = u_nickname + '@mail.ru'
	u_active = 1
	up_title = u_nickname;
	up_rating = random.randint(-15, 200)
	
	db_users = u_password + '|' + u_nickname + '|' + u_mail + '|' + str(u_active) + '\n'
	db_profiles = str(up_rating) + '|' + str(i + 2) + '|' + up_title + '\n'
	f_users.write(db_users);
	f_profiles.write(db_profiles)
	print('Created User #' + str(i + 1))

f_users.close()
f_profiles.close()

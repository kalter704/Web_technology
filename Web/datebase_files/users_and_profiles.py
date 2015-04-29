# -*- coding: utf-8 -*-
from datetime import datetime
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

dt_obj = datetime(2008, 11, 10, 17, 53, 59)
u_created = dt_obj.strftime("%Y-%m-%d %H:%M:%S")

for i in range(number_users):
	u_nickname = randomword(name_length_low, name_length_high)
	u_nickname += str(i % 1000)
	u_password = randomPassword(password_length)
	u_mail = u_nickname + '@mail.ru'
	u_active = 1
	#u_created = datetime.datetime.now
	#u_created = '2015-01-01 15:01:15'
	up_title = u_nickname;
	up_rating = random.randint(-15, 200)
	
	db_users = u_password + '|' + u_nickname + '|' + u_mail + '|' + str(u_active) + '|' + u_created +'\n'
	db_profiles = str(up_rating) + '|' + str(i + 2) + '|' + up_title + '\n'
	f_users.write(db_users);
	f_profiles.write(db_profiles)
	print('Created User #' + str(i + 1))

"""
da = datetime.now
print da.strftime("%Y-%m-%d %H:%M:%S")
"""
"""
dt_obj = datetime(2008, 11, 10, 17, 53, 59)
date_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
print date_str
"""
f_users.close()
f_profiles.close()

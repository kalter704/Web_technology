# -*- coding: utf-8 -*-
from ask.models import UserProfile
from django.contrib.auth.models import User

def isEmptyField(username, email, password, avatar):
	if username == '':
		return True
	if email == '':
		return True
	if password == '':
		return True
	if avatar == '':
		return True
	return False
	
def checkPassword(password, again_password):
	if password != again_password:
		return True
	return False
	
def isUserExist(username):
	is_exist = True
	try:
		u = User.objects.get(username = username)
	except:
		is_exist = False
	return  is_exist
	
def createProfileUser(username, email, password, avatar):
	u = User.objects.create_user(username, email, password)
	if avatar == None:
		avatar = 'Null'
	from pprint import pprint
	pprint(avatar)	
	up = UserProfile(title = username, user = u, rating = 0, avatar = avatar)
	up.save()
	
def isEmptyQuestionFields(f1, f2, f3):
	if f1 == '':
		return True
	if f2 == '':
		return True
	if f3 == '':
		return True
	return False

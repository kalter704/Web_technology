# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from ask.models import Question, Answer, Tag, UserProfile
from django.contrib.auth.models import User
import json
import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from pager import paginateObjects, paginatorIndex, positionOfAnswer
from check_form import isEmptyField, checkPassword, isUserExist, createProfileUser, isEmptyQuestionFields
from forms import ProfileUser, ProfileSettings, NewQuestion, NewAnswer

# Create your views here.

def home(request):
	string = "Hello world!!!"
	try:
		page = int(request.GET.get('page'))
	except ValueError:
		#raise Http404
		#render(request, 'error404.html')
		string = "<h3 style=\"color: red;\">Error404</h3>"
	return HttpResponse(string)

def home2(request, pk):
	#try:
	#	pk = int(pk)
	#except:
	#	raise Http404
	data = {
		'pk': int(pk),
	}
	return HttpResponse(json.dumps(data), content_type='application/json')

#questions = [
#	{'id': 1, 'title': 'Как построить лунапарк?', 'content': 'Самый актуальный вопрос современности - это как построить лунапарк!!!',
#	 'tags': ['moon', 'howto'], 'created': datetime.datetime.now()},
#	{'id': 2, 'title': 'Где взять малину?', 'content': 'где где где малина!!!',
#	 'tags': ['moon', 'howto'], 'created': datetime.datetime.now()},
#	{'id': 3, 'title': 'ЛЯЛЯЛЛЯЛЯ', 'content': 'лялялялл',
#	 'tags': ['moon', 'howto'], 'created': datetime.datetime.now()},
#]

#def index_temp(request):
#	context = {
#		'questions': Question.objects.popular()[:10]
#		#'questions': questions
#	}
#	return render(request, 'index.html', context)

def index(request):
	num_question_on_page = 3
	tag = request.GET.get('tag')
	#try:
	#	tag = request.GET['tag']
	#except KeyError:
	#	tag = None
	if tag == None:
		#question_list = Question.objects.date()
		question_list = Question.objects.popular()
	else:
		#question_list = Question.objects.filter(tags__text = tag).order_by('-rating')
		question_list = Question.objects.popular_by_tag(tag)
	questions = paginateObjects(request, question_list, num_question_on_page)
	'''
	prev = getPrev(questions.number)
	nex = getNext(questions.number, questions.paginator.num_pages)
	dot_first = dotFirst(questions.number)
	dot_last = dotLast(questions.number, questions.paginator.num_pages)
	'''
	pag = paginatorIndex(questions.number, questions.paginator.num_pages, tag)
	context = {
		#'questions': Question.objects.popular()[:10],
		#'questions': Question.objects.date()[:10],
		'questions': questions,
		'choice_tag': tag,
		'pag': pag
	}
	return render(request, 'index.html', context)

#def index(request):
#	return render(request, 'index.html', ())

def connectTags(q, tags):
	_tags = tags.split(',')
	for tag in _tags:
		tag = tag.strip(' ')
		t = Tag(text = tag)
		t.save()
		q.tags.add(t)

@login_required
def ask(request):
	form = NewQuestion()
	
	if request.POST:
		title = request.POST.get('title')
		text = request.POST.get('text')
		tags = request.POST.get('tags')

		form.fields['title'].initial = title
		form.fields['text'].initial = text
		form.fields['tags'].initial = tags
		
		is_empty_fields = False
		if isEmptyQuestionFields(title, text, tags):
			is_empty_fields = True
		
		if is_empty_fields:
			context = {
				'is_empty_fields': is_empty_fields,
				'form': form			
			}
			return render(request, 'ask.html', context)
		else:
			#tags.encode('utf-8')
			#connectTags(q, tags)
			#t = Tag(text = tags)
			#t.save()
			q = Question(title = title, text = text, author = request.user, rating = 0)
			q.save()
			connectTags(q, tags)
			#q.tags.add(t)
			q.save()
			id_question = q.id
			#return render(request, 'answer.html/' + str(id_question) + '/')
			#return HttpResponseRedirect('/answer/' + str(id_question) + '/')
			return redirect('/answer/' + str(id_question) + '/')
	return render(request, 'ask.html', {'form': form})

def none_answer(request):
	return render(request, 'error404.html', ())

def answer(request, pk): 
	form = NewAnswer()
	num_answer_on_page = 3
	pk = int(pk)
	question = Question.objects.get(id=pk)
	
	new_answer = False
	position_of_answ = 0
	
	if request.POST:
		text = request.POST.get('text')
		if text != '':
			a = Answer(question = question,	text = text, author = request.user)
			a.save()
			new_answer = True
			position_of_answ = a.id
	
	if new_answer:
		request.GET = {'page': 'last'}
	
	answers_list = Answer.objects.filter(question__id=pk)
	answers = paginateObjects(request, answers_list, num_answer_on_page)
	pag = paginatorIndex(answers.number, answers.paginator.num_pages)
	#print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	#print pag['dotFirst']
	#print pag['pr']
	#print answers.number
	#print pag['ne']
	#print pag['dotLast']
	context = {
		'question': question,
		'answers': answers,
		'pag': pag,
		'form': form,
		'new_asnwer': new_answer,
		'position': position_of_answ
	}
	#return redirect('/answer/' + str(pk))
	return render(request, 'answer.html', context)

def login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			next_page = request.POST.get('next_page')
			print(next_page)
			if (next_page == 'None' or next_page == ''):
				return redirect('/')
			else:
				return redirect(next_page)
		else:
			return  render(request, 'log_in.html', {'login_error' : True})
	try:
		next_page = request.GET['next']
	except:
		next_page = None
	return render(request, 'log_in.html', {'next_page': next_page})

def logout(request):
	auth.logout(request)
	return redirect('/')

def register(request):
	form = ProfileUser()
	
	if request.POST:
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		again_password = request.POST.get('again_password')
		#avatar = request.POST.get('avatar')
		avatar = request.FILES.get('avatar', None)

		form.fields['username'].initial = username
		form.fields['email'].initial = email
		
		is_empty_field = False
		is_wrong_pass = False
		is_user_exist = False
		
		if isEmptyField(username, email, password, avatar):
			is_empty_field = True
		if checkPassword(password, again_password):
			is_wrong_pass = True
		if isUserExist(username):
			is_user_exist = True
		#print(is_user_exist)
		
		if is_empty_field or is_wrong_pass or is_user_exist:
			context = {
				'form': form,
				'username': username,
				'email': email,
				'is_empty_field': is_empty_field,
				'is_wrong_pass': is_wrong_pass,
				'is_user_exist': is_user_exist
			}
			return render(request, 'register.html', context)
		else:
			createProfileUser(username, email, password, avatar)
			'''
			createProfileUser(form.cleaned_data['username'], 
							  form.cleaned_data['email'],
							  form.cleaned_data['password'],
							  form.cleaned_data['avatar'] )
			print('qwesacsd')
			'''
			
			
			return redirect('/')
			#return render(request, 'register.html', {'register': True})
			
			
			'''
			print('qwesacsd!!!!!!!!!')
			print(form.errors['username'])
			print(form.errors['email'])
			print(form.errors['password'])
			print(form.errors['avatar'])
			'''
			return render(request, 'register.html', {'form': form})
	return render(request, 'register.html', {'form': form})

@login_required
def settings(request):
	form = ProfileSettings()
	user = request.user
	
	form.fields['username'].initial = user
	form.fields['email'].initial = user.email
	
	if request.POST:
		username = request.POST.get('username')
		email = request.POST.get('email')
		avatar = request.FILES.get('avatar', None)
		print(avatar)
		
		if isEmptyField(username, email, '123456', avatar):
			context = {
				'form': form,
				'username': username,
				'email': email,
				'is_empty_field': True
			}
			return render(request, 'settings.html', context)
		else:
			is_change_prof = False
			if user != username:
				request.user.username = username
				is_change_prof = True
			if user.email != email:
				request.user.email = email
				is_change_prof = True
			if user.profile.avatar != avatar and avatar != None:
				from pprint import pprint
				pprint(avatar)
				request.user.profile.avatar = avatar
				is_change_prof = True
			if is_change_prof:
				request.user.save()
				request.user.profile.save()
				form.fields['username'].initial = user
				form.fields['email'].initial = user.email
				
	return render(request, 'settings.html', {'form': form})

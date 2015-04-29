# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from ask.models import Question, Answer, Tag
import json
import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

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
	
	
def paginateObjects(request, all_objects, num_on_page):
	print(all_objects)
	paginator = Paginator(all_objects, num_on_page)
	try:
		page = request.GET['page']
	except:
		page = 1
	#try:
	#page = paginator.num_pages
	try:
		pag_obj = paginator.page(page)
	except PageNotAnInteger:
		pag_obj = paginator.page(1)
	#except EmptyPage:
	#	pag_obj = paginator.page(1)
	#except InvalidPage:
	#	pag_obj = paginator.page(1)
	return pag_obj

def getPrev(num):
	n = []
	if num - 2 >= 1:
		n += [str(num - 2)]
	if num - 1 >= 1:
		n += [str(num - 1)]
	return n
	
def getNext(num, last):
	n = []
	if num + 1 <= last:
		n += [str(num + 1)]
	if num + 2 <= last:
		n += [str(num + 2)]
	return n
	
def dotFirst(num):
	n = ''
	if num - 4 >= 1:
		n += str(num - 4)
	elif num - 3 >= 1:
		n += str(num - 3)
	return n
	
def dotLast(num, last):
	n = ''
	if num + 4 <= last:
		n += str(num + 4)
	elif num + 3 <= last:
		n += str(num + 3)
	return n
	
def paginatorIndex(num, last, tag = None):
	if tag == None:
		tag = ''
	else:
		tag = 'tag=' + tag
	r = {
		'number': num,
		'pr': getPrev(num),
		'ne': getNext(num, last),
		'dotFirst': dotFirst(num),
		'dotLast': dotLast(num, last),
		'last': last,
		'tag': tag,
	}
	return r

def index(request):
	num_question_on_page = 3
	try:
		tag = request.GET['tag']
	except KeyError:
		tag = None
	if (tag == None):
		question_list = Question.objects.date()
	else:
		question_list = Question.objects.filter(tags__text = tag).order_by('-rating')
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

def ask(request):
	return render(request, 'ask.html', ())

def none_answer(request):
	return render(request, 'error404.html', ())

def answer(request, pk): 
	num_answer_on_page = 3
	pk = int(pk)
	question = Question.objects.get(id=pk)
	answers_list = Answer.objects.filter(question__id=pk) 
	answers = paginateObjects(request, answers_list, num_answer_on_page)
	pag = paginatorIndex(answers.number, answers.paginator.num_pages)
	print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	print pag['dotFirst']
	print pag['pr']
	#print answers.number
	print pag['ne']
	print pag['dotLast']
	context = {
		'question': question,
		'answers': answers,
		'pag': pag,
	}
	return render(request, 'answer.html', context)

def login(request):
	return render(request, 'log_in.html', ())

def register(request):
	return render(request, 'register.html', ())

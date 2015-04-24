# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from ask.models import Question, Answer, Tag
import json
import datetime

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
	try:
		tag = request.GET['tag']
	except KeyError:
		tag = None
	if (tag == None):
		question = Question.objects.date()[:10]
	else:
		question = Question.objects.filter(tags__text = tag).order_by('-rating')
	context = {
		#'questions': Question.objects.popular()[:10],
		#'questions': Question.objects.date()[:10],
		'questions': question,
		'choice_tag': tag,
	}
	return render(request, 'index.html', context)

#def index(request):
#	return render(request, 'index.html', ())

def ask(request):
	return render(request, 'ask.html', ())

def answer(request, pk):
	pk = int(pk)
	question = Question.objects.get(id=pk)
	answers = Answer.objects.filter(question__id=pk)
	context = {
		'question': question,
		'answers': answers,
	}
	return render(request, 'answer.html', context)

def login(request):
	return render(request, 'log_in.html', ())

def register(request):
	return render(request, 'register.html', ())

# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):    
    if(request.method=='GET'):
	output='hello world <br/>GET data:<br/> '
	for key,value in request.GET.items():
		output += key + ' = ' + value + '<br/>'         
        return HttpResponse(output)
    if(request.method=='POST'):      
        output='hello world <br/>POST data:<br/> '
	for key,value in request.POST.items():
		output += key + ' = ' + value + '<br/>'
        return HttpResponse(output)
        
#def index(request):
#	return render(request, 'index.html', ())

#def ask(request):
#	return render(request, 'ask.html', ())

#def answer(request):
#	return render(request, 'answer.html', ())

#def login(request):
#	return render(request, 'log_in.html', ())

#def register(request):
#	return render(request, 'register.html', ())

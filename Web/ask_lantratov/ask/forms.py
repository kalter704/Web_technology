# -*- coding: utf-8 -*-
from django import forms

class ProfileUser(forms.Form):
	username = forms.CharField(label='Логин', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	email = forms.EmailField(label='Mail', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	password = forms.CharField(label='Пароль', widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
	again_password = forms.CharField(label='Повторите пароль', widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
	avatar = forms.ImageField(label='Аватарка', widget = forms.ClearableFileInput(attrs = {'class': 'form-control'}))
	
class ProfileSettings(forms.Form):
	username = forms.CharField(label='Логин', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	email = forms.EmailField(label='Mail', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	avatar = forms.ImageField(label='Аватарка', widget = forms.ClearableFileInput(attrs = {'class': 'form-control'}))
	
class NewQuestion(forms.Form):
	title = forms.CharField(label='Заголовок', widget = forms.TextInput(attrs = {'class': 'form-control', 'style': 'margin: 0px; width: 385px;'}))
	text = forms.CharField(label='Текст', widget = forms.Textarea(attrs = {'class': 'form-control', 'rows': 10, 'style': 'margin: 0px; width: 385px; height: 264px;'}))
	tags = forms.CharField(label='Теги', widget = forms.TextInput(attrs = {'class': 'form-control', 'style': 'margin: 0px; width: 385px;'}))

class NewAnswer(forms.Form):
	text = forms.CharField(label='Текст', widget = forms.Textarea(attrs = {'class': 'form-control answer_text', 'rows': 10, 'style': 'margin: 0px; width: 584px; height: 264px;'}))

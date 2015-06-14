# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
import datetime
from ask.models import Question, Tag, Answer, UserProfile
from django.contrib.auth.models import User
import random, string
	
def find_popular_users():
	tags = Tag.objects.all()
	print(tags)
	the_most_popular_tag = Tag.objects.get(id = 1)
	numder_using_tag = 0
	for tag in tags:
		numder_using = 0
		questions = Question.objects.all()
		for question in questions:
			ques_tags = question.tags.all()
			for q_t in ques_tags:
				if q_t == tag:
					numder_using = numder_using + 1
		if numder_using_tag < numder_using:
			the_most_popular_tag = tag
			numder_using_tag = numder_using
	print(the_most_popular_tag.text + " " + str(numder_using_tag))
		
	
class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
		find_popular_users()

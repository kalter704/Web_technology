# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
import datetime
from ask.models import Question, Tag, Answer, UserProfile
from django.contrib.auth.models import User
import random, string
	
def find_popular_users():
	popular_users = UserProfile.objects.order_by('-rating')[:5]
	for user in popular_users:
		print("User: " + user.title + "\n Rating: " + str(user.rating) + "\n")
		
	
class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
		find_popular_users()

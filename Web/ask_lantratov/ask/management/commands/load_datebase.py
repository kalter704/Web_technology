# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from django.db import connection

class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
		#use = int(raw_input('Load Users?(1 - yes, 0 - no): '))
		prof = int(raw_input('Load Profiles?(1 - yes, 0 - no): '))
		ques = int(raw_input('Load Question?(1 - yes, 0 - no): '))
		tag = int(raw_input('Load Tags?(1 - yes, 0 - no): '))
		rel = int(raw_input('Load Relationships questions with tags?(1 - yes, 0 - no): '))
		ans = int(raw_input('Load Answers?(1 - yes, 0 - no): '))
		
		cursor = connection.cursor()
		print('Load datebase: ')
		#if(use == 1):
		#	print('Load Users...')
		#	cursor.execute("LOAD DATA LOCAL INFILE '/home/vasiliy/TechnoPark/GitHub/Web_technology/Web/datebase_files/users.txt' INTO TABLE auth_user FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' (password, username, email, is_active, created);")
			
		if(prof == 1):
			print('		Get Profiles...')
			cursor.execute("LOAD DATA LOCAL INFILE '/home/vasiliy/TechnoPark/GitHub/Web_technology/Web/datebase_files/profiles.txt' INTO TABLE ask_userprofile FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' (rating, user_id, title);")
		
		if(ques == 1):
			print('		Get Questions...')
			cursor.execute("LOAD DATA LOCAL INFILE '/home/vasiliy/TechnoPark/GitHub/Web_technology/Web/datebase_files/question.txt' INTO TABLE ask_question FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' (title, text, author_id, rating, created);")
		
		if(tag == 1):
			print('		Get Tags...')
			cursor.execute("LOAD DATA LOCAL INFILE '/home/vasiliy/TechnoPark/GitHub/Web_technology/Web/datebase_files/tag.txt' INTO TABLE ask_tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' (text);")
		
		if(rel == 1):
			print('		Get Relationships questions with tags...')
			cursor.execute("LOAD DATA LOCAL INFILE '/home/vasiliy/TechnoPark/GitHub/Web_technology/Web/datebase_files/questions_tags.txt' INTO TABLE ask_question_tags FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' (question_id, tag_id);")
		
		if(ans == 1):
			print('		Get Answer...')
			cursor.execute("LOAD DATA LOCAL INFILE '/home/vasiliy/TechnoPark/GitHub/Web_technology/Web/datebase_files/answer.txt' INTO TABLE ask_answer FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' (text, right_answer, author_id, question_id);")
		
		print('Datebase loaded!!!')

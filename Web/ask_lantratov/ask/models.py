from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.



class Tag(models.Model):
	text = models.CharField(max_length = 30)
	
	def __unicode__(self):
		return (str(self.id) + ' ' + self.text)


class QuestionManager(models.Manager):
	def popular(self):
		return self.get_queryset().order_by('-rating')
		
	def date(self):
		return self.get_queryset().order_by('-created')
		
	def popular_by_tag(self, tag):
		return self.get_queryset().filter(tags__text = tag).order_by('-rating')


class Question(models.Model):
	title = models.CharField(max_length = 80)
	text = models.TextField()
	author = models.ForeignKey(User)
	created = models.DateTimeField(default = datetime.datetime.now)
	rating = models.IntegerField(default = 0)
	tags = models.ManyToManyField(Tag)
	
	objects = QuestionManager()
	
	def __unicode__(self):
		return (str(self.id) + ' ' + self.title)
		
		
class Answer(models.Model):
	question = models.ForeignKey(Question)
	text = models.TextField()
	right_answer = models.BooleanField(default = False)
	author = models.ForeignKey(User)
	rating = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return (str(self.id) + ' ' + self.text)
	
class UserProfile(models.Model):
	title = models.CharField(max_length = 20, default = '')	
	user = models.OneToOneField(User, related_name='profile')
	rating = models.IntegerField()
	#avatar = models.CharField(max_length = 20, default = '')
	avatar = models.ImageField(upload_to = 'avatars/', null = True)
	#like = models.ManyToManyField(Likes)
	
	def get_avatar(self):
		if (self.avatar):
			return self.avatar.url
		else:
			return '/noAvatar.jpeg'
	
	def __unicode__(self):
		return (str(self.id) + ' ' + self.title)

'''
class Likes(models.Model):
	like = models.IntegerField(default = 0)
	answer = models.ForeignKey(Answer)
	type_like = models.CharField(max_length = 10, default = '')	
'''

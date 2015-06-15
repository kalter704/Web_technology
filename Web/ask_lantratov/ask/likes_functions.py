# -*- coding: utf-8 -*-
from ask.models import Question, Answer, Tag, UserProfile, LikesQuestion, LikesAnswer
from django.contrib.auth.models import User

def getLikeObject(ob_type, user, ob_id):
	if ob_type == 'question':
		likes = LikesQuestion.objects.filter(user__id = user.id).filter(id_question = ob_id)
	else:
		likes = LikesAnswer.objects.filter(user__id = user.id).filter(id_answer = ob_id)
	if not likes.exists():
		#like = LikesQuestion(user = user, like = 0, id_question = ob_id)
		if ob_type == 'question':
			return LikesQuestion(user = user, like = 0, id_question = ob_id)
		else:
			return LikesAnswer(user = user, like = 0, id_answer = ob_id)
	else:
		return likes[0]
		
def setLikes(action, rating, like):
	if action == 'like':
		if like.like != 1:
			rating = rating + 1
		return {'action' : 1,
				'rating' : rating
				}
	else:
		if like.like != -1:
			rating = rating - 1
		return {'action' : -1,
				'rating' : rating
				}

def getObject(ob_id, ob_type):
	if ob_type == 'question':
		return Question.objects.get(id = ob_id)
	else:
		return Answer.objects.get(id = ob_id)

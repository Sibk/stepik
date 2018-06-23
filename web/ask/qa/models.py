from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class QuestionManager(models.Manager):
#	def new(self):
#		return super(QuestionManager, self).new().all().order_by('-id')
		
#	def popular(self):
#		return super(QuestionManager, self).popular().all().order_by('-rating')
		
class Question(models.Model):
#	objects = QuestionManager()
	title = models.CharField(max_length = 100)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	likes = models.ManyToManyField(User, related_name = 'user_likes')

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

'''class QuestionManager(models.Model):
	def new(self):
		que = Question.objects.filter(Max(added_at))
		return que
	def popular(self):
		popular = Question.objects.all().order_by('-rating')
		return popular'''

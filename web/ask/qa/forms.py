from django import forms
from qa import models

class AskForm(forms.Form):
	title = forms.CharField(max_length = 100)
	text = forms.TextField()
	
	def clean_title(self):
		title = self.clean_data['title']
		if title is None:
			raise ValidationError('error, title is null')
		return title

	def save(self):
		title = self.clean_data['title']
		text = self.clean_data['text']
		post = models.Question(title = title, text = text)
		post.save()
		return post

class AnswerForm(forms.Form):
	text = forms.TextField()
	question = forms.IntegerField()


	def clean(self):
		text = self.clean_data['text']
		question = self.clean_data['question']
		if(text is None):
			raise ValidationError('error, text null')
		try:
			question = int(question)
		except ValueError:
			raise ValidationError('error int question')
		return text, question
	
	def save(self):
		text = self.clean_data['text']
		question = self.clean_data['question']
		post = models.Answer(text = text, question = question)
		return post		

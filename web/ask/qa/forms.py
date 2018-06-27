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

class AnswerForm(forms.Form):
	text = forms.TextField()
	question = forms.IntegerField()



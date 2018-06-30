from django import forms
from qa import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField(max_length = 100)
	text = forms.CharField()
	
	def clean_title(self):
		title = self.cleaned_data['title']
		if title is None:
			raise ValidationError('error, title is null')
		return title

	def save(self, request):
		title = self.cleaned_data['title']
		text = self.cleaned_data['text']
		post = models.Question(title = title, text = text, author = request.user)
		post.save()
		return post

class AnswerForm(forms.Form):
	text = forms.CharField()
	question = forms.IntegerField()


	def clean(self):
		text = self.cleaned_data['text']
		question = self.cleaned_data['question']
		if(text is None):
			raise ValidationError('error, text null')
		try:
			question = int(question)
		except ValueError:
			raise ValidationError('error int question')
		return text, question
	
	def save(self, request):
		text = self.cleaned_data['text']
		question = self.cleaned_data['question']
		post = models.Answer(text = text, question_id = question, author = request.user)
		return post		

class RegistrationForm(UserCreationForm):
	username = forms.CharField()
	password1 = forms.CharField()
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'password1', 'email')

	def save(self, commit = True):
		user = super(RegistrationForm, self).save(commit = False)
		if(commit):
			user.save()
		return user

class UserLoginForm(AuthenticationForm):
	username = forms.CharField()
	password = forms.CharField()	

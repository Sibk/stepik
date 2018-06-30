from django.shortcuts import render, HttpResponse, redirect
from qa.models import Question, Answer
from django.core.paginator import Paginator
from django.http import Http404
from qa.forms import AskForm, AnswerForm, RegistrationForm, UserLoginForm
from django.contrib import auth
import re
# Create your views here.

def test(request, *args, **kwargs):
	html = {}
	if(request.method == 'POST'):
		form = AskForm(data = request.POST)
		if(form.is_valid()):
			tt = form.save(request)
			html['form'] = form
			return redirect('/question/{}/'.format(tt.id))
	else:
		html['form'] = AskForm()
	return render(request, 'ask.html', html)

def test2(request, page):
	page = request.GET.get('page', 1)
	html = {}
	res = Question.objects.all().order_by('-id')
	paginator = Paginator(res, 10)
	cont = paginator.page(page)
	html['cont'] = cont
	return render(request, 'test2.html', html)


def test3(request):
	html = {}
	page = request.GET.get('page', 1)
	res = Question.objects.all().order_by('-rating')
	paginator = Paginator(res, 10)
	cont = paginator.page(page)
	html['cont'] = cont
	return render(request, 'test2.html', html)


def test4(request):
	html ={}
	page = request.GET.get('page', 1)
	page = re.findall(r'\d+', request.path)[0]
	if(request.method == 'POST'):
		form = AnswerForm()
		if(form.is_valid()):
			form.save(request)
			html['form'] = form
			return redirect('/question/{}/'.format(page))		
	else:
		try:
			res = Question.objects.get(id = page)
			ss = Answer.objects.filter(question = res)
			html['qst'] = res
			html['ans'] = ss
			html['form'] = AnswerForm()
			return render(request, 'test3.html', html)
		except Question.DoesNotExist:
			raise Http404
	return HttpResponse('OK')

def signup(request):
	html = {}
	if(request.method == 'POST'):
		form = RegistrationForm(request.POST)
		if(form.is_valid()):
			form.save()
			login(request)
			return redirect('/')
	else:
		form = RegistrationForm()
		html['form'] = form
	return render(request, 'signup.html', html)

def login(request):
	html = {}
	if(request.method == 'POST'):
		form = UserLoginForm(request.POST)
		if(form.is_valid()):
			auth.login(request. form.user_cache)
			return redirect('/')
	else:
		form = UserLoginForm()
		html['form'] = form
	return render(request, 'login.html', html)

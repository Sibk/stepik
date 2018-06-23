from django.shortcuts import render, HttpResponse
from qa.models import Question
from django.core.paginator import Paginator, Answer
# Create your views here.

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def test2(request, page):
	html = {}
	res = Question.objects.all()
	paginator = Paginator(res, 10)
	cont = paginator.page(page)
	html['cont'] = cont
	return render(request, 'test2.html', html)


def test3(request, page):
	html = {}
	res = Question.objects.all().order_by('-rating')
	paginator = Paginator(res, 10)
	cont = paginator.page(page)
	html['cont'] = cont
	return render(request, 'test2.html', html)


def test4(request, page):
	html ={}
	try:
		res = Question.objects.get(id = page)
		ss = Answer.objects.filter(question = res)
	except Question.DoesNotExist:
		return Http404
	html['qst'] = res
	html['ans'] = ss
	return render(request, 'test3.html', html)
	

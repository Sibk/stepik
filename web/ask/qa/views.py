from django.shortcuts import render, HttpResponse
from qa.models import Question, Answer
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

def test(request, *args, **kwargs):
	return HttpResponse('OK')

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


def test4(request, page):
	html ={}
	try:
		res = Question.objects.get(id = page)
		ss = Answer.objects.filter(question = res)
	except Question.DoesNotExist:
		raise Http404
		
	html['qst'] = res
	html['ans'] = ss
	return render(request, 'test3.html', html)
	

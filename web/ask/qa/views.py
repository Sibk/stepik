from django.shortcuts import render, HttpResponse

# Create your views here.

def test(request, *args, **kwargs):
	return HttpResponse('OK')

from django.http import HttpResponse
from django.shortcuts import render

def index_new(request):
	return HttpResponse("Hello, again World.you're at the polls index.")


def new_func(request):
	data={'name': 'Ali',
			'post': 'SE'}

	return render(request, 'new_temp.html', data) 



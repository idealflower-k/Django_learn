from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

articles = {
	'sports': 'Sports page',
	'finance': 'Finance page',
	'politics': 'Politics page',
}

def news_view(request, topic):
	try:
		return HttpResponse(articles[topic])
	except:
		raise Http404("No such topic")

def add_view(request, num1, num2):
	# domain.com/first_app/num1/num2/
	add_result = num1 + num2
	result = f"{num1} + {num2} = {add_result}"
	return HttpResponse(str(result))

def num_page_view(request, num_page):
	try:
		topic = list(articles.keys())[num_page]
		return HttpResponseRedirect(reverse('topic-page', args=[topic]))
	except:
		raise Http404("No such page")

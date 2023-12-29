from django.shortcuts import render
from django.views import View
from .models import Todo
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

class TodoListView(View):
	def get(self, request):
		todos = Todo.objects.all()
		return JsonResponse(list(todos.values()), safe=False)

	def post(self, request):
		data = json.loads(request.body)
		todo = Todo.objects.create(title=data['title'])
		return JsonResponse({'id': todo.id, 'title': todo.title, 'completed': todo.completed})

class TodoDetailView(View):
	def get_object(self, id):
		try:
			return Todo.objects.get(pk=id)
		except Todo.DoesNotExist:
			return None

	def get(self, request, id):
		todo = self.get_object(id)
		if todo is None:
			return HttpResponse(status=404)
		return JsonResponse({'id': todo.id, 'title': todo.title, 'completed': todo.completed})
	
	def put(self, request, id):
		todo = self.get_object(id)
		if todo is None:
			return HttpResponse(status=404)
		data = json.loads(request.body)
		todo.title = data.get('title', todo.title)
		todo.completed = data.get('completed', todo.completed)
		todo.save()
		return JsonResponse({'id': todo.id, 'title': todo.title, 'completed': todo.completed})
	
	def delete(self, request, id):
		todo = self.get_object(id)
		if todo is None:
			return HttpResponse(status=404)
		todo.delete()
		return HttpResponse(status=204)

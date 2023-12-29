from django.urls import path
from .views import TodoListView, TodoDetailView

app_name = 'Todo'

urlpatterns = [
	path('', TodoListView.as_view(), name='list_create_todos'),
	path('<int:id>/', TodoDetailView.as_view(), name='detail_todos'),
]


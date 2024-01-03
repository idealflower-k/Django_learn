from rest_framework import viewsets, permissions, status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BooksAPI(APIView):
	def get(self, request):
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		print(request.data)
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
	def get(self, request, bid):
		book = get_object_or_404(Book, bid=bid)
		serializer = BookSerializer(book)
		return Response(serializer.data, status=status.HTTP_200_OK)

class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	lookup_field = 'bid'

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
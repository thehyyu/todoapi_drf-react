from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    # Used for read-only endpoints to represent a collection of model instances.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    # Used for read-only endpoints to represent a single model instance.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

from .models import Todo, Category
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


# Todo ViewSet
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer
from rest_framework import serializers
from .models import Todo, Category


# Todo serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
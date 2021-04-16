from django.shortcuts import render

# restframewok
from rest_framework import viewsets

# Project
from Todo.models import Todo
from Todo.serializers import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

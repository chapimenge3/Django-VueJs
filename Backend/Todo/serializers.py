# Restframework
from django.db.models import fields
from rest_framework import serializers

# Project
from Todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
    
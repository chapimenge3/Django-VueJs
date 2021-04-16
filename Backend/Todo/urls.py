from django.urls import  path, include
from rest_framework import routers

# restframework
from rest_framework.routers import DefaultRouter

# Project 
from Todo.views import TodoViewset

router = DefaultRouter()
router.register(r'todo', TodoViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

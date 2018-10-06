from django.urls import path,include
from rest_framework import routers
from .views import Emp_serializer, Emp_ViewSet

rou = routers.DefaultRouter()
rou.register('',Emp_ViewSet)

urlpatterns =[
    path('emp/', include(rou.urls))
]
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Emp_serializer
# Create your views here.
from django.contrib.auth.models import User
def index(request):
    return render(request, 'index.html',{})

class Emp_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Emp_serializer
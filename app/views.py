from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
from .models import Students
from .serializers import studentsSerilizers
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin

class StudentList(ListModelMixin,GenericAPIView):
    queryset=Students.objects.all()
    serializer_class=studentsSerilizers

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)






















    

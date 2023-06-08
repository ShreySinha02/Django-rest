from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
from .models import Students
from .serializers import studentsSerilizers
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def StudenntsView(request):
    # if request.method =='GET':
    #     json_data=request.body
    #     stream=io.BytesIO(json_data)
    #     pythondata=JSONParser().parse(stream)
    #     id=pythondata.get('id',None)
    #     if id is not None:
    #         stu=Students.objects.get(id=id)
    #         serializer=studentsSerilizers(stu)
    #         return JsonResponse(serializer.data,safe=False)
    #     stu=Students.objects.all()
    #     serializer=studentsSerilizers(stu,many=True)
    #     return JsonResponse(serializer.data,safe=False)
    if request.method =='POST':
        # json_data=request.body
        # stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(request)
        print(pythondata)
        serializer=studentsSerilizers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            msg={'suc':'sucess'}
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse("msg", status=400)
    return HttpResponse('Hii')
    

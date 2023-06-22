from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Mysql_model as Student
# Create your views here.

def get_student(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from student")
        students=cursor.fetchall()
        print('Students',students)

    print('students here are',students)
    data=[{'name':student[0],'marks':student[3]} for student in students]
    print("Students are",students)
    return JsonResponse(data, safe=False)

def hello(request):
    return HttpResponse("Hello, World")

@csrf_exempt
def add_user(request):
    if request.method=='POST':
        payload=json.loads(request.body)
        print('Payload is',payload)
        with connection.cursor() as cursor:
            cursor.execute(f"insert into student (name,subject,marks) values('{payload['name']}','{payload['subject']}',{payload['marks']})")
            inserted=cursor.fetchall()
            print("Inserted",inserted)
        return JsonResponse({'message':"User added Successfully"},safe=False)


def get_detail(request):
    params=request.GET
    print("Params is",params)
    with connection.cursor() as cursor:
        cursor.execute(f"select * from student where name='{request.GET.get('user')}'")
        details=cursor.fetchall()
        print('details',details)
        print(type(details))
    return JsonResponse({'message':'It is Working'},safe=False)

def get_models(request):
    if request.method=='GET':
        print('PARAMS--------',request.GET['name'])
        key=request.GET['name']
        row=Student.objects.get(name=key)
        name=Student.objects.filter(name='July')
        print('Length of fields',Student._meta.fields)
        data={field.name: getattr(row, field.name) for field in Student._meta.get_fields()}
        return JsonResponse(data)

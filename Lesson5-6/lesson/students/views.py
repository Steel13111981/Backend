from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import Student


def my_view(request):
    if request.method == 'get':
        return HttpResponse('result')


class MyView(View):
    def get(self, request):
        students = Student.objects.all()
        students_data=[]
        for student in students:
            students_data.append({
                "name":student.name
            })
        
        return JsonResponse({"data":students_data})   
    
    def post(self, request):
        return HttpResponse('result11')   

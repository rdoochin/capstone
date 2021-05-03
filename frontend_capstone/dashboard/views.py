from django.shortcuts import render
from .models import Student
from django.template import context

def get(self, request):
    data = Student.objects.all()
    return render(request, 'dashboard/index.html', {'data': data})

def index(request):
    latest_question_list = Student.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'dashboard/index.html', context)
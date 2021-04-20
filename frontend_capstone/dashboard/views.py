from django.shortcuts import render
from django.http import HttpResponse
# from .models import Question
from .models import Student
from django.template import context
from django.http import Http404


def index(request):
    latest_question_list = Student.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # might need to pass in the student info as the context (if not a class)
    return render(request, 'dashboard/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def detail(request, question_id):
    try:
        question = Student.objects.get(pk=question_id)
    except Student.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'dashboard/detail.html', {'question': question})


# def index(request):
#     data = Student.objects.all()
#     stu = {
#         "student_number": data
#     }

#     return render(request, "dashboard/templates/dashboard/index.html", stu)

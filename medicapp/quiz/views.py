from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    question_list = Question.objects.order_by('question_text')
    template = loader.get_template('quiz/index.html')
    context = {
        'question_list': question_list,
    }

    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("This is Question %s." % question_id)

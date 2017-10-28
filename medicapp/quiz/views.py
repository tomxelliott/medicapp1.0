from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Question, Choice


def index(request):
    question_list = Question.objects.order_by('question_text')
    template = loader.get_template('quiz/index.html')
    context = {
        'question_list': question_list,
    }

    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})


def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    return render(request, 'quiz/answer.html', {
        'question': question,
        'choice': selected_choice,
    })
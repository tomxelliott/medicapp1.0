from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from models import UserProfile
from forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import Topic, Question, Choice, User


def index(request):
    """
    Generate the homepage view
    Pass the full list of Topics ordered from A-Z.
    :param request: HTTP request passed to function.
    :return: The context required for the home page.
    """
    topic_list = Topic.objects.order_by('topic_text')
    template = loader.get_template('quiz/index.html')

    context = {
        'topic_list': topic_list,
    }

    return HttpResponse(template.render(context, request))


@login_required
def question(request, topic_id):
    """
    This function fetches all of the questions for a given topic selected by the user.
    :param request: HTTP request from index.html page.
    :param topic_id: The id of the Topic chosen by the user.
    :return: List of questions for a given topic...
                Where none, return message to specify that.
    """
    question_list = Question.objects.filter(topic=topic_id).order_by('pk')
    template = loader.get_template('quiz/question.html')

    context = {
        'question_list': question_list,
    }

    return HttpResponse(template.render(context, request))


@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'quiz/detail.html', {'question': question})


@login_required
def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    next_question_id = int(question_id) + 1
    next_question_id = unicode(next_question_id)

    if Question.objects.filter(pk=next_question_id).exists():
        return render(request, 'quiz/answer.html', {
            'question': question,
            'choice': selected_choice,
            'next_question_id': next_question_id,
        })
    else:
        return render(request, 'quiz/answer.html', {
            'question': question,
            'choice': selected_choice,
        })


@login_required
def out_of_questions(request):
    topic_list = Topic.objects.order_by('topic_text')
    template = loader.get_template('quiz/out_of_questions.html')

    context = {
        'topic_list': topic_list,
    }

    return HttpResponse(template.render(context, request))

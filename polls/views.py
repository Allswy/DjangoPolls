from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'polls/detail.html', {'question': question, 'choices': choices})

def results(request, question_id):
    response = "You're looking at the result for question %s" % question_id
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting for question %s" % question_id)

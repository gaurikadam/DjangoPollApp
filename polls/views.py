from django.shortcuts import render
from django .template import loader
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    # template = loader.get_template
    context = {
        'latest_question_list' : latest_question_list
    }
    return render (request,'polls/index.html',context)
    # context = {
    #     'latest_question_list' : latest_question_list
    # }

    # output = ', '.join([q.question_text for q in latest_question_list])
  

def detail(request,question_id):
    # # return HttpResponse("you are lokking at question %s. ", % question_id )
    # # try:
    question = get_object_or_404(Question, pk=question_id)
    # return this with render 
    # except Question.DoesNotExist:
    #     raise Http404 ("Question does not exist")
    return render (request, 'polls/detail.html',{'question': question})

def results(request, question_id):

    return HttpResponse("You're looking results  question %s." % question_id)

def votes(request, question_id):

    return HttpResponse("You're looking results  question %s." % question_id)
from django.shortcuts import render
from django .template import loader
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question,Choice
from django.views import generic
from django.urls import reverse

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')[:5]
#     # template = loader.get_template
#     context = {
#         'latest_question_list' : latest_question_list
#     }
#     return render (request,'polls/index.html',context)
#     # context = {
#     #     'latest_question_list' : latest_question_list
#     # }

#     # output = ', '.join([q.question_text for q in latest_question_list])
  

# def detail(request,question_id):
#     # # return HttpResponse("you are lokking at question %s. ", % question_id )
#     # # try:
#     question = get_object_or_404(Question, pk=question_id)
#     # return this with render 
#     # except Question.DoesNotExist:
#     #     raise Http404 ("Question does not exist")
#     return render (request, 'polls/detail.html',{'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):

        return render(request,'polls/detail.html',
        {
            'question': question,
            'error message' : "you didnt select a choice.",
        })
    else:
        selected_choice.votes += 1    
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args= (question_id,)))

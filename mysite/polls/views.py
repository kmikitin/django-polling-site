# with render you don't need HttpResponse or loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    # Creates the context dictionary objects
    context = {'latest_question_list': latest_questions_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # returns a 404 error if there's no object
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on questions %s." % question_id)

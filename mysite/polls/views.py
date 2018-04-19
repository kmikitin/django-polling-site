# with render you don't need HttpResponse or loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.post lets you access submitted data by key name
        # w/choice returns the ID of the selected choice as a string
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # ALWAYS RETURN A REDIRECT when working with post data
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

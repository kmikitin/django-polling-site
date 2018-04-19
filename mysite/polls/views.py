# with render you don't need HttpResponse or loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.

# these classes are examples of the generic views in Django
# ListView will display a lits of objects
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return the last five published questions (not including those set to be published in the future.)
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# DetailView will display a detail of a page for a particular type of object
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        # Excludes any questions that aren't published
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

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

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from qa.models import Question
from qa.forms import AnswerForm 
from django.core.urlresolvers import reverse
 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form_s = form.save()
            url = reverse('question_detail', args=[pk])
            return HttpResponseRedirect(url)
        else:
            return HttpResponse('123')
    else:
        form = AnswerForm(initial={'question': pk})
        return render(request, 'question_detail.html', {
                'question': question,
                'form': form,
                })
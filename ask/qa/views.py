from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from qa.models import Question
 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_detail.html', {
                'question': question,
                })
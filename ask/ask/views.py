from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from qa.models import Question
from qa.forms import AskForm, AnswerForm
from django.core.urlresolvers import reverse

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    page = paginator.page(page)
    return paginator, page

@require_GET
def post_list(request):
    posts = Question.objects.all().order_by('-added_at')
    paginator, page = paginate(request, posts)
    return render(request, 'post_list.html',
                {'posts': page.object_list,
                'paginator': paginator,
                'page': page,
    })

@require_GET
def popular(request):
    posts = Question.objects.all().order_by('-rating')
    paginator, page = paginate(request, posts)
    return render(request, 'post_list.html',
                {'posts': page.object_list,
                'paginator': paginator,
                'page': page,
    })

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form_s = form.save()
            url = reverse('question_detail', args=[form_s.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'ask.html', {
                'form': form,
        })
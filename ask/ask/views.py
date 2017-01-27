from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from qa.models import Question

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
    posts = Question.objects.all().order_by('-id')
    paginator, page = paginate(request, posts)
    return render(request, 'post_list.html',
                {'posts': posts,
                'paginator': paginator,
                'page': page,
    })

@require_GET
def popular(request):
    posts = Question.objects.all().order_by('-rating')
    paginator, page = paginate(request, posts)
    return render(request, 'post_list.html',
                {'posts': posts,
                'paginator': paginator,
                'page': page,
    })
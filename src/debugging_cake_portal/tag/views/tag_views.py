from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tag.models.tag_model import Tag
from django.core.paginator import Paginator, EmptyPage


class TagListView(ListView):
    model = Tag
    context_object_name = 'tag_list'
    template_name = "tag_list_template.html"


class TagDetailView(DetailView):
    model = Tag
    context_object_name = 'tag_report'
    template_name = "tag_detail_template.html"


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Tag.objects.all()
    # categories = Tag.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('notReviewed')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(title__icontains=title_or_author_query)
                       | Q(author__name__icontains=title_or_author_query)
                       ).distinct()

    if is_valid_queryparam(view_count_min):
        qs = qs.filter(views__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(views__lt=view_count_max)

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(categories__name=category)

    if reviewed == 'on':
        qs = qs.filter(reviewed=True)

    elif not_reviewed == 'on':
        qs = qs.filter(reviewed=False)

    return qs


def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return Tag.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > Tag.objects.all().count():
        return False
    return True


def BootstrapFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'categories': Tag.objects.all()
    }
    return render(request, "bootstrap_form_template.html", context)


@login_required
def tag_index(request):
    tag_items = Tag.objects.all()
    p = Paginator(tag_items, 5)

    print('NUMBER OF PAGES')
    print(p.num_pages)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {'tags': page}
    return render(request, 'tag_list_template.html', context)



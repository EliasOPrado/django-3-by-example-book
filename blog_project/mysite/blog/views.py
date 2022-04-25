from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.
def post_list(request):
    object_list = Post.objects_published.all()
    paginator = Paginator(object_list, 3)# three post for each page.
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if the page is not an integer, show the first page.
        posts = paginator.page(1)
    except EmptyPage:
        # if the page is being out of intervals, 
        # shows the last result page.
        posts = paginator.page(paginator.num_pages)
        
    context = {'page':page, 'posts':posts}
    return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = Post.objects.get(slug=post,
                             status='published', 
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {'post':post}
    return render(request, 'blog/post/detail.html', {'post':post})
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.
class PostListView(ListView):
    queryset = Post.objects_published.all()
    context_object_name = 'posts'
    paginated_by = 3
    template_name = 'blog/post/list.html'



def post_detail(request, year, month, day, post):
    post = Post.objects.get(slug=post,
                             status='published', 
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {'post':post}
    return render(request, 'blog/post/detail.html', {'post':post})
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import EmailPostForm
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


def post_share(request, post_id):
    # Acquire the post based on id.
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # form was submitted.
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields are validated.
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']} recomends you read "\
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com')

        else:
            form = EmailPostForm()
        context = {'post':post, 'form':form}
        return render(request, 'blog/post/share.html', context)

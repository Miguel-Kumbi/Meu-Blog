from django.shortcuts import get_object_or_404, render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'blog/home.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)
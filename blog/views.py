from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'blog/home.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            form.save_m2m() # Relacionamentos Many-to-Many (Tag) precisam de tratamento separado quando usamos .save()

            return redirect(post_detail, slug=post.slug)
    else:
        form = PostForm()
    context = {'form':form}

    return render(request, 'blog/post_form.html', context)
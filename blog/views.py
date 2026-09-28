from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
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


def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

            return redirect(post_detail, slug=post.slug)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'post': post}

    return render(request, 'blog/post_form.html', context)


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.delete()

        return redirect('home')

    context = {'post': post}

    return render(request, 'blog/post_confirm_delete.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') # Pegar dados enviados do formulário.
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) # Verificar as credencias no BD.
        if user is not None:
            login(request, user) # Criar/Atualizar a sessão de autenticação.

            return redirect('home')

        context = {'error': 'username ou password inválidos!'}

        return render(request, 'blog/login.html', context)

    return render(request, 'blog/login.html')


def logout_view(request):

    logout(request)

    return redirect('home')
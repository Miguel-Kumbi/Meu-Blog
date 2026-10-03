from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone
from .models import Post
from .forms import PostForm

def home(request):
	# posts = Post.objects.all()
	posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
	context = {'posts': posts}

	return render(request, 'blog/home.html', context)


def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post': post}

	return render(request, 'blog/post_detail.html', context)


@login_required # Verifica se há uma autenticacão válida antes de executar  a view. Senão redireciona para o login.
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


@login_required
def post_update(request, slug):
	post = get_object_or_404(Post, slug=slug)

	if post.author != request.user:
		return HttpResponseForbidden ('Sem permissão para editar este post.')

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)

		if form.is_valid():
			form.save()

			return redirect(post_detail, slug=post.slug)
	else:
		form = PostForm(instance=post)
	context = {'form': form, 'post': post}

	return render(request, 'blog/post_form.html', context)


@login_required
def post_delete(request, slug):
	post = get_object_or_404(Post, slug=slug)

	if post.author != request.user:
		return HttpResponseForbidden ('Sem permissão para deletar este post.')

	if request.method == 'POST':
		post.delete()

		return redirect('home')

	context = {'post': post}

	return render(request, 'blog/post_confirm_delete.html', context)


@login_required
def post_publish(request, slug):
	post = get_object_or_404(Post, slug=slug)

	if post.author != request.user:
		return HttpResponseForbidden('Você não tem permissão para publicar este Post.')

	if request.method == 'POST':
		post.published_at = timezone.now()
		post.save()

		return redirect('post_detail', slug=post.slug)

	return render(request, 'blog/post_confirm_publish.html', {'post': post})


@login_required
def drafts(request):
	posts = Post.objects.filter(author=request.user, published_at__isnull=True).order_by('-published_at')
	context = {'posts': posts}
	return render(request, 'blog/drafts.html', context)

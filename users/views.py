from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST) # Pegar dados enviados do formulário.

		if form.is_valid():
			login(request, form.get_user()) # Criar/Atualizar a sessão de autenticação.

			return redirect('home')
	else:
		form = AuthenticationForm()
	context = {'form': form}
	return render(request, 'users/login.html', context)


def logout_view(request):

	logout(request) # Fecha a sessão de autenticacão

	return redirect('home')

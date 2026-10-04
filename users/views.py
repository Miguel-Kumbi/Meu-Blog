from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from .forms import LoginForm, RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form,}

    return render(request, 'users/register.html', context)


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request, data=request.POST) # Pegar dados enviados do formulário.

		if form.is_valid():
			login(request, form.get_user()) # Criar/Atualizar a sessão de autenticação.

			return redirect('home')
	else:
		form = LoginForm()
	context = {'form': form}
	return render(request, 'users/login.html', context)


def logout_view(request):

	logout(request) # Fecha a sessão de autenticacão

	return redirect('home')

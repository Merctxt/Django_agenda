from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usúario registrado')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if form.is_valid():
        if form.has_changed():
            form.save()  # Salva os dados do formulário
            messages.success(request, 'Usuário atualizado com sucesso.')
            return redirect('contact:user_update')  # Redireciona para a página de perfil, por exemplo
        else:
            messages.warning(request, 'Nada alterado.')
            return redirect('contact:user_update')
    
    
    
    return redirect('contact:login')

def login_view(request):
    form = AuthenticationForm(request)


    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Usúario logado com sucesso!')
            return redirect('contact:index')
        else:
            messages.error(request, 'Login inválido!')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Usúario deslogado com sucesso!')
    return redirect('contact:login')